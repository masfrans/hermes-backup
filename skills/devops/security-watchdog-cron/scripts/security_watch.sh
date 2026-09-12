#!/bin/bash
# Security watchdog VPS - template teruji (sesi 2026-08, VPS Ibramsyah).
# Dipanggil cron Hermes (no_agent=true): stdout kosong = diam, non-empty = kirim.
# Hanya lapor IP BARU + IP lama yang masih menyerang (anti-spam per-IP state).
# Jadwal direkomendasikan: 0 */2 * * * (tiap 2 jam) via cronjob tool.

STATE_FILE="/root/.hermes/scripts/.security_watch_ipstate"

get_banned() {
  fail2ban-client status sshd 2>/dev/null | grep -oP 'Banned IP list:\s*\K.*' | tr ' ' '\n' | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' | sort -u
}

get_active_attackers() {
  journalctl -u ssh --since "15 min ago" 2>/dev/null | grep "Failed password" | grep -oP 'from \K[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort -u
}

ALERTS=""
BANNED_NOW=$(get_banned)
ACTIVE_NOW=$(get_active_attackers)

REPORTED=""
[ -f "$STATE_FILE" ] && REPORTED=$(cat "$STATE_FILE" 2>/dev/null)

if [ -n "$BANNED_NOW" ]; then
  NEW_IPS=""
  ACTIVE_KNOWN=""
  for ip in $BANNED_NOW; do
    if ! echo "$REPORTED" | grep -qx "$ip"; then
      NEW_IPS="$NEW_IPS $ip"
    fi
  done
  for ip in $BANNED_NOW; do
    if echo "$REPORTED" | grep -qx "$ip" && echo "$ACTIVE_NOW" | grep -qx "$ip"; then
      ACTIVE_KNOWN="$ACTIVE_KNOWN $ip"
    fi
  done
  [ -n "$NEW_IPS" ] && ALERTS="${ALERTS}
🆕 FAIL2BAN: $(echo $NEW_IPS | wc -w) IP BARU diblokir (brute force SSH):${NEW_IPS}"
  [ -n "$ACTIVE_KNOWN" ] && ALERTS="${ALERTS}
🔁 IP yg sdh dilaporkan MASIH mencoba login:${ACTIVE_KNOWN}"
  echo "$BANNED_NOW" > "$STATE_FILE"
else
  rm -f "$STATE_FILE"
fi

# Alert SSH count WAJIB sertakan IP + jumlah per IP (user pernah komplain
# "kenapa IP nya tidak kelihatan")
FAILED=$(journalctl -u ssh --since "15 min ago" 2>/dev/null | grep -c "Failed password" || echo 0)
if [ "$FAILED" -ge 5 ]; then
  FAILED_IPS=$(journalctl -u ssh --since "15 min ago" 2>/dev/null | grep "Failed password" | grep -oP 'from \K[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort | uniq -c | sort -rn | awk '{printf "%s(x%s) ", $2, $1}' | head -c 400)
  ALERTS="${ALERTS}
⚠️ SSH: ${FAILED} percobaan login gagal dalam 15 menit terakhir
   IP: ${FAILED_IPS}"
fi

# Cek lain (opsional): sudo gagal, load tinggi, disk penuh, miner, user baru
# (pola sama seperti versi lengkap - lihat SKILL.md)

[ -n "$ALERTS" ] && echo "$ALERTS"
