# Hermes Agent Backup

## Isi Backup
- `config.yaml` - Konfigurasi utama Hermes
- `SOUL.md` - Soul/personality Hermes
- `.env` - Environment variables (KEYS REDACTED - paste manual)
- `skills/` - Semua skill
- `memories/MEMORY.md` - Memory
- `memories/USER.md` - User profile
- `scripts/` - Script-script
- `cron/jobs.json` - Cron jobs
- `platforms/` - Platform configs

## Restore Instructions
1. Install ulang Hermes Agent
2. Copy file-file ini ke `/root/.hermes/`
3. Setup ulang API keys (token tidak ikut terbackup)
4. Setup ulang WhatsApp bridge
5. Setup cron jobs

## Catatan
- `.env` perlu di-setup ulang karena security
- WhatsApp session perlu di-setup ulang
- API keys perlu di-input ulang
