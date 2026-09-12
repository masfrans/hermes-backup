# WhatsApp bridge (Baileys) troubleshooting — worked examples (2026-08)

Real incidents on a Sumopod VPS (Ubuntu, systemd user gateway, WhatsApp bot "Mas Bro").

## Case 1: Bot paired but ignored every message (allowlist_mismatch)

Symptom: pairing succeeded (`hermes whatsapp` → QR scan → `✅ WhatsApp connected!`), but every user message got no reply.

Bridge log (`~/.hermes/whatsapp/bridge.log`):

```
✅ WhatsApp connected!
{"event":"ignored","reason":"allowlist_mismatch","chatId":"163041840726263@lid",...}
{"event":"ignored","reason":"allowlist_mismatch","chatId":"32203715125442@lid",...}
```

Root cause: `.env` had `WHATSAPP_ALLOWED_USERS=foranyone`. The bridge does NOT treat "foranyone" as a magic keyword — it matches it as a literal username, so nobody matched and all messages were dropped. The correct allow-everyone value is a single asterisk:

```
WHATSAPP_ALLOWED_USERS=*
```

After gateway restart, bridge log prints `🔒 Allowed users: *` — that line confirms the fix, not the "connected" line.

## Case 2: System notifications leaking into WA chat

User: "jangan kirimkan pesan seperti ini di bot wa" (don't send system/progress notices on WA — answers only).

Messages seen in the WA chat:
1. `📬 No home channel is set for Whatsapp ... type /sethome` — one-time prompt; fixed by setting `WHATSAPP_HOME_CHANNEL=32203715125442@lid` in `.env` (or user types `/sethome` in the WA chat).
2. `🔄 Switched to fallback model: hallo/gpt-5.6-luna via custom → deepseek-v4-flash via custom` — emitted through the gateway status path (status_callback → `_prepare_gateway_status_message`), NOT covered by `display.platforms.whatsapp.*`. Suppressed by adding `r"|switched\s+to\s+fallback\s+model"` to the `_TELEGRAM_NOISY_STATUS_RE` regex in `/usr/local/lib/hermes-agent/gateway/run.py` (~line 140). Source edit — lost on Hermes update, re-apply after upgrades.
3. `⚠️ Gateway shutting down – Your current task will be interrupted.` — suppressed by `hermes config set platforms.whatsapp.gateway_restart_notification false` (per-platform config read in `_notify_active_sessions_of_shutdown`).

Full silence set for WA (all via `hermes config set`):

```
display.platforms.whatsapp.tool_progress 'off'
display.platforms.whatsapp.interim_assistant_messages false
display.platforms.whatsapp.long_running_notifications false
display.platforms.whatsapp.busy_ack_enabled false
display.platforms.whatsapp.busy_ack_detail false
display.platforms.whatsapp.credits_notices false
platforms.whatsapp.gateway_restart_notification false
```

## Case 3: Reconnect loop (reason 408)

```
⚠️  Connection closed (reason: 408). Reconnecting in 3s...   (repeated many times)
✅ WhatsApp connected!
```

408 = request timeout; repeated loops mean the WhatsApp session is unstable: phone with the bot number offline, WA unlinked from "Perangkat tertaut", or rate-limited. If the last line is `✅ WhatsApp connected!` the bridge recovered; if it keeps cycling, re-pair: run `hermes whatsapp`, scan the QR with the bot number.

## Case 4: link-preview-js missing (non-fatal)

```
Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'link-preview-js' imported from
.../whatsapp-bridge/node_modules/@whiskeysockets/baileys/lib/Utils/link-preview.js
```

Only URL-preview generation fails; messages still flow. Fix if previews needed:

```bash
cd /usr/local/lib/hermes-agent/scripts/whatsapp-bridge && npm install link-preview-js
```

## Diagnosis order for "WA bot not replying"

1. `tail -30 ~/.hermes/whatsapp/bridge.log` — look for `allowlist_mismatch`, `Connection closed`, `Error`.
2. `tail -15 ~/.hermes/logs/gateway.log` — gateway side; `inbound message: platform=whatsapp` confirms the message arrived at the gateway.
3. `ps aux | grep -iE 'whatsapp|baileys'` — bridge process must be alive.
4. `grep '^WHATSAPP_ALLOWED_USERS' ~/.hermes/.env` — must be `*` for open bot.
5. Restart gateway (systemd-run method, see SKILL.md) after any .env/config change — the gateway loads `.env` once at startup.
