#!/bin/bash
# Security watchdog untuk VPS - diam kalau aman, alert kalau ada tanda bahaya.
# Dipanggil tiap 15 menit oleh cron Hermes (no_agent=true).
# Output non-empty = kirim notif; empty = diam. Dedup: alert yang sama tidak dikirim ulang.

ALERTS=""

# 1. Fail2ban: IP yang sedang diblokir dari brute force SSH
BANNED=$(fail2ban-client status sshd 2>/dev/null | grep -oP 'Currently banned:\s+\K[0-9]+' || echo 0)
if [ "$BANNED" -gt 0 ]; then
  BANLIST=$(fail2ban-client status sshd 2>/dev/null | grep -A8 'Banned IP list' | tail -5 | tr '\n' ' ')
  ALERTS="${ALERTS}
⚠️ FAIL2BAN: ${BANNED} IP sedang diblokir (brute force SSH): ${BANLIST}"
fi

# 2. Percobaan login SSH gagal dalam 15 menit terakhir
FAILED=$(journalctl -u ssh --since "15 min ago" 2>/dev/null | grep -c "Failed password" || echo 0)
if [ "$FAILED" -ge 5 ]; then
  ALERTS="${ALERTS}
⚠️ SSH: ${FAILED} percobaan login gagal dalam 15 menit terakhir (kemungkinan brute force)"
fi

# 3. Percobaan sudo gagal dalam 15 menit terakhir
SUDOFAIL=$(journalctl --since "15 min ago" 2>/dev/null | grep -cE "sudo.*(incorrect password|authentication failure)" || true)
if [ "${SUDOFAIL:-0}" -ge 3 ] 2>/dev/null; then
  ALERTS="${ALERTS}
⚠️ SUDO: ${SUDOFAIL} percobaan sudo gagal dalam 15 menit terakhir"
fi

# 4. Beban server tinggi (load average 1 menit) - indikasi miner
LOAD=$(cat /proc/loadavg | awk '{print $1}')
LOADINT=$(echo "$LOAD * 100 / 1" | bc 2>/dev/null || echo 0)
NCPU=$(nproc)
THRESH=$((NCPU * 4))
if [ "$LOADINT" -gt "$THRESH" ] && [ "$LOADINT" -gt 400 ]; then
  ALERTS="${ALERTS}
⚠️ BEBAN SERVER TINGGI: load ${LOAD} (${NCPU} CPU) - kemungkinan ada proses mencurigakan"
fi

# 5. Disk hampir penuh
DISK=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
if [ "$DISK" -gt 90 ]; then
  ALERTS="${ALERTS}
⚠️ DISK HAMPIR PENUH: ${DISK}% terpakai"
fi

# 6. Proses mencurigakan (crypto miner dll)
MINERS=$(ps aux | grep -iE 'xmrig|minergate|kryptex|nicehash|cpuminer|ethminer' | grep -v grep | awk '{print $11}' | head -3 | tr '\n' ' ')
if [ -n "$MINERS" ]; then
  ALERTS="${ALERTS}
🚨 PROSES MENINGKAT: ${MINERS}"
fi

# 7. User baru (uid >= 1000, kecuali yang sudah dikenal)
KNOWN_USERS="ubuntu admin deploy www-data"
NEWUSERS=""
for u in $(awk -F: '$3 >= 1000 {print $1}' /etc/passwd); do
  if ! echo "$KNOWN_USERS" | grep -qw "$u"; then
    HOMEDIR=$(eval echo ~$u)
    if [ -d "$HOMEDIR" ] && [ "$(stat -c %Y "$HOMEDIR" 2>/dev/null)" -gt "$(( $(date +%s) - 86400 ))" ]; then
      NEWUSERS="$NEWUSERS $u"
    fi
  fi
done
if [ -n "$NEWUSERS" ]; then
  ALERTS="${ALERTS}
⚠️ USER BARU terdeteksi: ${NEWUSERS}"
fi

# Dedup: alert yang sama persis dengan kiriman terakhir TIDAK dikirim ulang (anti-spam).
STATE_FILE="/root/.hermes/scripts/.security_watch_last"

if [ -n "$ALERTS" ]; then
  SIG=$(echo "$ALERTS" | md5sum | awk '{print $1}')
  LAST_SIG=""
  [ -f "$STATE_FILE" ] && LAST_SIG=$(cat "$STATE_FILE" 2>/dev/null)
  if [ "$SIG" != "$LAST_SIG" ]; then
    echo "$ALERTS"
    echo "$SIG" > "$STATE_FILE"
  fi
else
  # Aman: reset state supaya ancaman yang hilang lalu muncul lagi = dianggap baru
  rm -f "$STATE_FILE"
fi
