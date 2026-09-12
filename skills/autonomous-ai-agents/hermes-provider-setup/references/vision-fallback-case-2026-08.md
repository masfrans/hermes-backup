# Vision Fallback Case: Quota 429 → Blind Main Model → Apology Relayed to User

Worked case (2026-08, WhatsApp bot "Mas Bro"): a user sent an image and the bot
replied with a raw vision-model apology in Mandarin ("抱歉，我无法看到您提到的图片…"),
making the bot look broken. Owner complained: "jangan tampilkan pesan seperti ini
ke orang lain yg chat km".

## Diagnosis trail

1. Gateway log: `Image routing: text (mode=text). Pre-analyzing 1 image(s) via vision_analyze.`
   — the gateway pre-analyzes every inbound image and injects the result as context.
2. Agent log (`~/.hermes/logs/agent.log`) — the smoking gun:
   ```
   Auxiliary vision (async): payment error on gemini (Gemini HTTP 429 (RESOURCE_EXHAUSTED):
   You exceeded your current quota...)
   Auxiliary vision: payment error on gemini — falling back to main agent model
   main-agent(custom) (deepseek-v4-flash)
   ```
   → configured vision provider (Gemini free tier) hit daily quota; the auxiliary
   client fell back to the MAIN agent model, which is text-only (deepseek-v4-flash).
3. The blind model answered the image prompt with "I can't see the image" (the
   vision tool reports `success: true` for ANY model response), and
   `_enrich_message_with_vision` (gateway/run.py) wrapped it as
   `[The user sent an image~ Here's what I can see: <apology>]` → the main agent
   relayed that text verbatim to the user.

## Why every fallback candidate failed (tested same day)

| Endpoint | Result | Meaning |
|---|---|---|
| Gemini (GOOGLE_API_KEY) | 429 RESOURCE_EXHAUSTED | free-tier daily quota; resets ~midnight PT |
| Sumopod glm-5-turbo | 400 `messages.content.type invalid, allowed ['text']` | text-only model |
| Sumopod MiniMax-M2.7-highspeed | replies "cannot see the image" | no vision despite accepting the request |
| Sumopod gemini-*/glm-5v | 403 `key not allowed to access model` | key allowlist = only the 5 listed models |
| Hallorouter (any model) | `inference_unavailable` / `model_temporarily_unavailable` | service-wide outage at the time |
| Groq llama-3.2-11b-vision | 403 `Access denied. Please check your network settings` | geo-block from Indonesian IP |

Takeaway: with no OpenRouter/Nous/DeepInfra key, the vision auto-detect chain
(OpenRouter → Nous → DeepInfra → main model) always lands on the text-only main
model when the configured provider fails. Re-probe endpoints with
`scripts/vision_probe.py` before wiring anything into `auxiliary.vision.*`.

## Fixes applied

1. **User-facing guard (system prompt level):** extended
   `agent.platform_hints.whatsapp.append` with: if an image can't be analyzed,
   NEVER relay the error/apology text (including foreign-language text) or tool
   names; reply naturally, e.g. "Maaf, aku nggak bisa lihat gambarnya. Coba
   kirim ulang ya 🙏". Same rule added to the identity file
   (`~/.hermes/scripts/wa_bot_identity.md`) and memory.
2. **Restore vision properly:** get a fresh free Gemini API key (AI Studio) or
   point `auxiliary.vision.provider/model` at a verified vision-capable endpoint.

## Lesson

A model-level instruction ("don't relay X") stored only in memory or a sidecar
file is unreliable with weaker main models; the enforcement point is the system
prompt via `agent.platform_hints` (see hermes-server-ops
`references/platform-hints-persona-injection.md` for the full mechanism).
