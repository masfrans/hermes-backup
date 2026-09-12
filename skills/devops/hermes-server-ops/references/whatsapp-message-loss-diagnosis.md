# Diagnosa "Pesan WA Tidak Dibalas" (message loss di layer bridge)

Worked example (2026-08-16): user di chat WhatsApp bilang "kenapa tidak ada respon".
Bot SUDAH mengirim clarify (terlihat di screenshot user jam 01:03 WIB), tapi balasan
user ("tidak jadi", 01:49 WIB) tidak pernah diproses.

## Pola diagnosa (grep gateway.log per chat_id)
1. `grep -n "<chat_id>" /root/.hermes/logs/gateway.log | tail`
   - **Inbound ada, tapi TIDAK ada "response ready" setelahnya** = pesan tidak pernah
     sampai ke gateway → drop di layer bridge (koneksi WhatsApp tidak stabil sesaat),
     BUKAN masalah agent, BUKAN allowlist.
   - Inbound ada + response ready ada, tapi user tidak menerima = masalah pengiriman
     egress (cek bridge.log, status koneksi).
   - Inbound tidak ada sama sekali padahal user yakin sudah kirim = pesan hilang di
     bridge → cek `~/.hermes/whatsapp/bridge.log` (lihat juga
     references/whatsapp-quiet-mode-2026-08.md soal allowlist `*`).
2. Cek sesi/transkrip: `session_search(session_id=...)` — clarify terkirim tapi
   `messages_after: 0` = bot sedang MENUNGGU jawaban user (bukan proses jalan).
3. Konversi timestamp Unix → WIB: `datetime.utcfromtimestamp(ts + 7*3600)` untuk
   mencocokkan jam di screenshot user.

## Solusi
- Minta user kirim ulang pesannya (paling cepat).
- Kalau perlu sesi baru dengan prompt/config baru: `hermes sessions delete <session_id> --yes`
  (gateway self-heal, sesi baru dibuat otomatis saat pesan berikutnya).
- Kalau sering terjadi: pantau koneksi bridge (bridge.log), pertimbangkan re-pair.

## Kirim pesan WA dari server (uji/notifikasi manual)
`hermes send -t "whatsapp:<chat_id>" "teks"` — chat_id format `xxx@lid`;
daftar target: `hermes send --list whatsapp`. Pesan tercatat sebagai pesan
assistant di sesi target (berguna untuk tes sapaan/perilaku bot dari sisi lain).
