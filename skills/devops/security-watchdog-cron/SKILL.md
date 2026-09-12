---
name: security-watchdog-cron
description: "Cron watchdog VPS: lapor hanya IP baru & aktivitas berulang."
version: 1.0.0
platforms: [linux]
---

# Security Watchdog Cron (laporan anti-spam)

Pola cron watchdog keamanan VPS (no_agent=true, script stdout = pesan ke chat)
yang hanya melaporkan perubahan BARU - tidak mengulang status lama.

## Trigger

- Membuat/memperbaiki cron security watchdog VPS (fail2ban, brute force SSH)
- User komplain laporan cron berulang-ulang (IP sama terus dilaporkan)
- User minta "laporkan hanya yang baru / jangan ulang yang sudah dilaporkan"

## Pola State File (dedup IP)

Script cron (contoh: `~/.hermes/scripts/security_watch.sh`) menyimpan state di
file (mis. `~/.hermes/scripts/.security_watch_ipstate`):

1. `get_banned()`: daftar IP banned saat ini dari `fail2ban-client status sshd`
2. `get_active_attackers()`: IP dengan "Failed password" di `journalctl -u ssh --since "15 min ago"`
3. Bandingkan banned sekarang vs state (IP yang sudah dilaporkan):
   - IP banned tapi TIDAK di state → 🆕 LAPOR sebagai IP baru
   - IP banned DAN di state DAN aktif menyerang lagi → 🔁 LAPOR "masih mencoba"
   - IP banned di state tapi tidak aktif → TIDAK diulang (diam)
4. Update state = daftar banned saat ini (IP lepas ban otomatis hilang dari state;
   kalau muncul lagi = dianggap baru)

Ini mencegah: daftar 50 IP yang sama dikirim tiap tick.

## Format Laporan

```
🆕 FAIL2BAN: 3 IP BARU diblokir (brute force SSH): ip1 ip2 ip3
🔁 IP yg sdh dilaporkan MASIH mencoba login: ip4 ip5
⚠️ SSH: 12 percobaan login gagal dalam 15 menit terakhir
   IP: ip1(x6) ip4(x4) ip6(x2)
```

Alert SSH count WAJIB menyertakan daftar IP + jumlah percobaan per IP
(format `ip(xN)`), bukan hanya angka total - user pernah komplain "kenapa IP
nya tidak kelihatan".

## Pitfall

- Jangan dedup dengan md5 seluruh pesan (daftar 50 IP berubah sedikit → semua
  terkirim ulang). Dedup per-IP via state file.
- Ambil IP dari log `Failed password ... from X` via
  `grep -oP 'from \K[0-9.]+'` lalu `sort | uniq -c | sort -rn`
- Ambang alert SSH (>= 5 percobaan/15 menit) - sesuaikan sensitivitas
- Cron no_agent=true: stdout kosong = diam (tidak kirim apa-apa); gunakan ini
  untuk mode watchdog
- Script harus `chmod +x`; state file dibuat otomatis oleh script
