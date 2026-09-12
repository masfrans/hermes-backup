---
name: linux-ssh-security
description: "Harden & monitor Linux SSH: fail2ban, UFW, botnet analysis."
version: 1.0.0
platforms: [linux]
---

# Linux SSH Security: Hardening & Attack Monitoring

## When to Use
- User melaporkan brute force ("kenapa banyak yang coba masuk VPS", "cek IP ini dari mana")
- User minta hardening VPS (firewall, fail2ban, aturan ban)
- Setup pemantauan keamanan / watchdog

## Langkah Hardening
1. Install fail2ban: `apt-get install -y fail2ban && systemctl enable --now fail2ban`
2. Tulis `/etc/fail2ban/jail.local` (template di bawah), lalu `systemctl restart fail2ban`
3. Verifikasi: `fail2ban-client status sshd` (tampilkan banned IP list)
4. Aktifkan UFW: `ufw default deny incoming`, `ufw allow 22/tcp`, `80`, `443`, `ufw enable`
5. Setup watchdog cron (lihat `scripts/security_watch.sh`)

## Template jail.local (fail2ban)
```
[sshd]
enabled = true
port = 22
filter = sshd
logpath = /var/log/auth.log
maxretry = 3        # jumlah gagal sebelum ban
bantime = 259200    # detik: 300=5mnt, 18000=5jam, 86400=1hari, 259200=3hari
findtime = 600      # jendela deteksi (10 menit)
```
Setelah edit: `systemctl restart fail2ban && fail2ban-client status sshd`.

## Membaca Log Serangan
- `journalctl -u ssh --since "30 min ago" | grep -E "Accepted|Failed"`
- Sesi aktif: `who` dan `ss -tnp | grep ':22'`
- Tutup sesi SSH: `kill <pid>` dari proses `sshd: root@pts/N` (pid dari `ps aux | grep 'sshd:.*@'`)

## Membedakan User Asli vs Botnet (PENTING)
- **Botnet**: ledakan "Failed password", target seragam (root/ubuntu/admin/nobody), interval teratur, IP muter-muter dalam subnet/provider sama (misal 45.148.10.x TECHOFF, TechTies Amsterdam), port sumber tinggi/random
- **User asli**: "Accepted password" (SUKSES), jumlah sedikit. Aplikasi SSH mobile (SSH Easy dll) tampil dari DUA IP: IP proxy (provider cloud seperti DigitalOcean US) + IP ISP rumah/direct. Dua-duanya normal.
- Sebelum menuduh penyusup: cocokkan waktu login sukses dengan aktivitas user (jam berapa dia bilang masuk). Login sukses dari proxy cloud + ISP lokal = pola SSH Easy, bukan penyusup.
- IP di daftar "Failed" bisa juga IP user sendiri (kesalahan ketik password saat login) - jangan asal ban IP lokal.

## Geolokasi IP
Pakai ipinfo.io (bukan whois, lebih cepat dan terstruktur):
```python
import urllib.request, json
req = urllib.request.Request(f"https://ipinfo.io/{ip}/json", headers={"User-Agent": "curl/8.0"})
d = json.loads(urllib.request.urlopen(req, timeout=15).read())
# d.get('city'), d.get('region'), d.get('country'), d.get('org')
```

## Pitfalls
- JANGAN pernah ganti password VPS tanpa izin eksplisit user (preferensi user: password tidak boleh disentuh)
- Jangan ban permanen tanpa konfirmasi: user bisa di belakang proxy (IP berubah-ubah)
- Volume serangan botnet adalah "suara latar" normal internet untuk semua server SSH publik, bukan serangan pribadi - sampaikan ini ke user biar tidak panik
- Selalu verifikasi config fail2ban kebaca setelah restart (status menunjukkan jail aktif)

## Watchdog
Script watchdog lengkap dengan dedup (diam saat aman, alert hanya untuk ancaman baru/berubah): `scripts/security_watch.sh`. Jadwalkan via cron Hermes tiap 15 menit dengan no_agent=true (stdout non-empty = notif, empty = diam).
