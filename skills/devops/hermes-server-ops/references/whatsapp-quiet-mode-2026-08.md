# Worked example: WhatsApp paired but silent (2026-08-16)

Real incident: WhatsApp bot paired successfully (`✅ WhatsApp connected!` in bridge.log)
but every message was ignored. Telegram worked fine.

## Symptom
- `hermes whatsapp` pairing succeeded; bot showed connected.
- Sending a message to the bot number produced NO reply, no error in gateway.log.
- User reported "wa belum aktif" / "sudah kirim pesan tapi tidak ada balasan".

## Root cause #1: allowlist value
`~/.hermes/whatsapp/bridge.log` showed:
```
🔒 Allowed users: foranyone
✅ WhatsApp connected!
{"event":"ignored","reason":"allowlist_mismatch","chatId":"163041840726263@lid","senderId":"163041840726263@lid"}
```
`WHATSAPP_ALLOWED_USERS=foranyone` was parsed as a literal username, not a wildcard.
The bridge source (`scripts/whatsapp-bridge/allowlist.js`) documents the real magic value:
- `*` = allow everyone (consistent with `SIGNAL_GROUP_ALLOWED_USERS`)
- empty list = NO ONE allowed (secure default, #8389)
- anything else = literal match against expanded WhatsApp identifiers

Fix: `WHATSAPP_ALLOWED_USERS=*` in `.env`, then restart gateway.

## Root cause #2: system notices reaching the bot chat
After the allowlist fix, the owner saw three categories of system chatter they didn't want:
1. "📬 No home channel is set for Whatsapp ... Type /sethome" — one-time prompt; fixed by
   `WHATSAPP_HOME_CHANNEL=32203715125442@lid` in `.env` (or `/sethome` in the WA chat).
2. "🔄 Switched to fallback model: hallo/gpt-5.6-luna via custom → deepseek-v4-flash via custom"
   — emitted via agent `status_callback("lifecycle", ...)`; passes the gateway noise filter
   (`_TELEGRAM_NOISY_STATUS_RE` in `gateway/run.py`) because that regex doesn't include it.
   Suppressed by adding `r"|switched\s+to\s+fallback\s+model"` to the regex (source patch).
3. "⚠️ Gateway shutting down / restarting — Your current task will be interrupted."
   — per-platform toggle: `platforms.whatsapp.gateway_restart_notification: false` in config.yaml.

Plus the display-level quieting for the platform (replies only, no progress bubbles):
```yaml
display:
  platforms:
    whatsapp:
      tool_progress: 'off'
      interim_assistant_messages: false
      long_running_notifications: false
      busy_ack_detail: false
      busy_ack_enabled: false
      credits_notices: false
```

## Key lesson
A gateway can be fully "connected" on WhatsApp yet drop every message at the bridge
layer due to allowlist semantics. The gateway.log shows NOTHING about it — always check
`~/.hermes/whatsapp/bridge.log` first. And `*` (not `foranyone`, not empty) is the
"allow everyone" value.
