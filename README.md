# 🧬 Hermes Agent Backup

Backup ini berisi semua konfigurasi, skill, memory, dan script dari bot AI Hermes yang berjalan di VPS.

**Tanggal backup:** 12 September 2026
**Ukuran:** ~11 MB
**Jumlah file:** 594 file

---

## 📦 Apa yang Sudah Di-Backup?

| File/Folder | Isinya | Perlu Setup Ulang? |
|---|---|---|
| `config.yaml` | Pengaturan utama bot (model AI, provider, dll) | ❌ Sudah include |
| `SOUL.md` | Personalitas & karakter bot | ❌ Sudah include |
| `skills/` | Semua kemampuan bot (15+ kategori skill) | ❌ Sudah include |
| `MEMORY.md` | Memory jangka panjang bot | ❌ Sudah include |
| `USER.md` | Profil user & preferensi | ❌ Sudah include |
| `jobs.json` | Daftar cron job (task terjadwal) | ⚠️ Perlu setup ulang |
| `scripts/` | Script-script bantu (loker, OCR, pajak, dll) | ❌ Sudah include |

---

## ⚠️ Apa yang TIDAK Bisa Di-Backup?

### 1. API Keys & Tokens ( demi keamanan)

`**File: .env**`

File ini berisi API keys seperti:
- Sumopod API key (untuk AI)
- Apify API token (untuk scraping Twitter)
- GitHub token
- Vercel token

**Mengapa tidak di-backup?** Karena ini adalah "password" untuk layanan eksternal. Menyimpan password di backup adalah risiko keamanan.

**Yang perlu dilakukan:** Catat semua API key/token yang pernah dipakai dan siap untuk input ulang.

---

### 2. WhatsApp Session

`**Folder: whatsapp/**

WhatsApp session adalah "login" bot ke WhatsApp. Setiap HP/akun WhatsApp punya session unique yang terikat device.

**Mengapa tidak bisa di-backup?** WhatsApp mendeteksi jika account di-login di banyak device sekaligus. Transfer session bisa menyebabkan akun terkunci.

**Yang perlu dilakukan:** Setup ulang WhatsApp bridge di VPS baru (过程 sekitar 5 menit dengan QR code).

---

### 3. Google OAuth Token

`**File: google_token.json**`

Token ini adalah "login" ke Google account untuk akses Drive, Docs, Sheets.

**Mengapa tidak bisa di-backup?** Token OAuth punya expiry dan terikat dengan device ID.

**Yang perlu dilakukan:** Re-authenticate Google account di VPS baru.

---

## 🔄 Langkah Restore (VPS Baru)

Estimasi waktu: **30-60 menit**

---

### Step 1: Install Ulang Hermes Agent

Di VPS baru, install Hermes Agent:

```bash
# Install Hermes Agent
npm install -g hermes-agent

# Verifikasi installation
hermes --version
```

---

### Step 2: Clone Backup dari GitHub

```bash
# Clone repo backup
git clone https://github.com/masfrans/hermes-backup.git /tmp/hermes-backup

# Copy ke folder Hermes
cp -r /tmp/hermes-backup/* ~/.hermes/
```

---

### Step 3: Setup Ulang API Keys

File `.env` perlu dibuat ulang. Buat file baru:

```bash
nano ~/.hermes/.env
```

Isi dengan format berikut (ganti `YOUR_KEY_HERE` dengan key asli):

```env
# Sumopod AI (LLM Provider)
SUMOPOD_BASE_URL=https://ai.sumopod.com/v1
SUMOPOD_API_KEY=YOUR_SUMOPOD_API_KEY_HERE

# Apify (Twitter Scraper)
APIFY_API_TOKEN=YOUR_APIFY_TOKEN_HERE

# GitHub
GH_TOKEN=YOUR_GITHUB_TOKEN_HERE

# Vercel
VERCEL_TOKEN=YOUR_VERCEL_TOKEN_HERE
```

**Simpan:** Tekan `Ctrl+X`, lalu `Y`, lalu `Enter`

---

### Step 4: Setup Ulang WhatsApp Bridge

```bash
# Jalankan setup WhatsApp
hermes platforms setup whatsapp

# Ikuti instruksi di layar:
# 1. Buka WhatsApp di HP
# 2. Settings > Linked Devices > Link a Device
# 3. Scan QR code yang muncul di terminal
```

---

### Step 5: Setup Ulang Google OAuth (untuk Drive/Docs)

Jika butuh akses Google Drive/Docs:

```bash
# Cek status
python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --check

# Jika expired, re-authenticate
python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py
```

Ikuti instruksi di terminal untuk authorize via browser.

---

### Step 6: Setup Cron Jobs

Dari file `jobs.json`, buat ulang cron jobs:

```bash
# Lihat daftar cron jobs
cat ~/.hermes/cron/jobs.json
```

Cron jobs yang pernah disetup:
- Security watch (cek login attempt mencurigakan)

Untuk setup ulang, hubungi admin atau lihat dokumentasi cron.

---

### Step 7: Verifikasi Semua Berfungsi

```bash
# Test bot berjalan
hermes gateway run

# Test akses Telegram
# Kirim pesan ke bot - harusnya respons

# Test skill
# Tanyakan sesuatu ke bot yang butuh skill tertentu
```

---

## 📞 Butuh Bantuan?

Jika ada error atau bingung, Screenshoot/telepon admin dengan:
1. Error message yang muncul
2. Langkah yang sudah dilakukan
3. Screenshot terminal (jika ada)

---

## 🔐 Checklist Keamanan

Setelah restore selesai, pastikan:

- [ ] `.env` sudah di-setup dengan API keys yang valid
- [ ] WhatsApp bridge sudah terhubung
- [ ] GitHub token sudah disetup (untuk pull/push)
- [ ] Security watch cron sudah aktif

---

## 📝 Catatan Penting

1. **Jangan share backup ini** ke orang yang tidak berhak - berisi konfigurasi dan memory pribadi
2. **API keys bersifat rahasia** - jangan pernah kirim ke orang lain
3. **Rutin backup** - setiap ada perubahan signifikan, sebaiknya backup ulang

---

*Backup dibuat: 12 September 2026*
*Repo: https://github.com/masfrans/hermes-backup*
