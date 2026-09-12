# SSH Attack Investigation & IP Tracing

Workflow terbukti untuk menjawab "cek IP ini dari mana", "kenapa banyak yang coba masuk VPS", dan membedakan botnet vs login user sendiri.

## 1. Agregasi serangan (journalctl + Python Counter)
```python
import subprocess, re
from collections import Counter
out = subprocess.run(["journalctl", "-u", "ssh", "--since", "24 hours ago"],
                     capture_output=True, text=True).stdout
attempts = re.findall(r"Failed password for (\S+) from ([\d.]+) port (\d+)", out)
accepted = re.findall(r"Accepted password for (\S+) from ([\d.]+) port (\d+)", out)
ips = Counter(a[1] for a in attempts)
users = Counter(a[0] for a in attempts)
# ipinfo lookup beruntun: ThreadPoolExecutor(max_workers=5), header User-Agent wajib
```

## 2. Login sukses per waktu (konfirmasi ke user)
```bash
journalctl -u ssh --since "2026-08-14 23:15" | grep "Accepted"
# tampilkan tabel: waktu UTC -> WIB, IP, sumber (proxy/direct)
```

## 3. Pola botnet yang sudah terverifikasi (server Ibramsyah)
- **TECHOFF SRV LIMITED (AS48090, Amsterdam)** + **TechTies Inc. (AS197170, Amsterdam)**: dua provider paling sering; subnet 45.148.10.x, 195.178.110.x, 91.92.x
- Provider lain teramati: Host Baltic (LT), ZORNTECH (PL), UNMANAGED (RO), Awas.ovh (DE), Henan Mobile (CN), Comcast rumah (US)
- Target: root > ubuntu > admin; interval ~5-6 menit; 3-10 percobaan beruntun lalu pindah IP
- **Botnet ini NORMAL untuk semua VPS dengan port 22 terbuka** - bukan serangan pribadi; scan internet global

## 4. Pola login user sendiri (Ibramsyah)
- `146.190.49.157` (DigitalOcean US) = **proxy SSH Easy** (aplikasi SSH HP yang route lewat server US)
- `103.84.231.74` (PT Cemerlang Multimedia, Bandung) = **direct** dari jaringan rumah
- SSH Easy: IP bisa berganti-ganti (auto-select proxy, pindah WiFi/seluler). IP proxy hosting (DO/Vultr) + port sumber acak + sesi pendek = wajar, bukan penyusup
- Cara bedakan cepat: user = `Accepted` 1-2x; botnet = `Failed` puluhan kali

## 5. Kelola/tutup sesi SSH
```bash
who                        # sesi aktif + asal IP
ss -tnp | grep ':22'       # koneksi ESTAB
ps aux | grep 'sshd:.*@'   # pid sesi
kill <pid>                 # tutup sesi tertentu
```

## 6. Hasil verifikasi dari sesi ini (untuk konteks)
- 540 gagal / 34 IP unik dalam ~13 jam; puncak serangan 06:00-07:00 UTC
- Semua login sukses (7x) = user sendiri via SSH Easy (4x proxy DO, 3x direct Bandung)
