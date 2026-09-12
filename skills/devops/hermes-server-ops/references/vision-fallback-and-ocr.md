# Vision Gagal: Diagnosis, Fallback, dan OCR Lokal

Worked example (2026-08): user kirim gambar di WhatsApp, bot membalas apologi aneh
berbahasa Mandarin ("抱歉, saya tidak bisa melihat gambar..."). Screenshot dikirim
owner: "jangan tampilkan pesan seperti ini ke orang lain".

## Gejala
- Bot membalas gambar dengan teks error/apologi (bahasa asing atau Indonesia)
  yang tidak natural, bukan deskripsi gambar.
- vision_analyze (tool langsung) juga balas apologi alih-alih deskripsi.

## Akar masalah (rantai fallback)
1. `tools/vision_tools.py` mengirim gambar base64 ke aux vision provider
   (config `auxiliary.vision.*`).
2. Provider vision gagal (contoh: Gemini HTTP 429 RESOURCE_EXHAUSTED = quota
   key habis) → auxiliary_client fallback ke MAIN AGENT MODEL.
3. Kalau main model TEXT-ONLY (contoh deepseek-v4-flash via Sumopod), model
   tidak menerima pixel gambar → balas apologi.
4. Gateway `_enrich_message_with_vision` (gateway/run.py ~23493) menganggap
   SEMUA hasil `success: true` sebagai deskripsi valid dan inject sebagai
   "[The user sent an image~ Here's what I can see: <apologi>]" → model utama
   meneruskannya ke user.

## Diagnosis (cek agent.log dulu)
```bash
grep -n "Auxiliary vision\|falling back" /root/.hermes/logs/agent.log | tail
```
- "payment error on gemini (Gemini HTTP 429 ...)" → key vision quota habis.
- "falling back to main agent model ... (deepseek-v4-flash)" → fallback ke
  model text-only = penyebab apologi diteruskan.

## Tes endpoint mana yang bisa terima gambar
Jalankan `scripts/test_vision_endpoints.py` (support file skill ini): kirim
base64 test image ke tiap provider/model. Pola hasil yang pernah terlihat:
- Sumopod (litellm): model text-only tolak `content.type` image_url
  ("参数非法, 取值范围 ['text']"); key dibatasi ke model list tertentu.
- Hallorouter: bisa down total (inference_unavailable / model_temporarily_unavailable
  untuk SEMUA model, termasuk teks) — cek dulu layanan teks sebelum andalkan.
- Groq: bisa ke-block jaringan (Access denied).
- Fallback chain auto vision: openrouter → nous → deepinfra (butuh key masing-masing).

## Fallback: OCR lokal (tesseract)
Saat vision mati, gambar berisi teks (dokumen/CV/screenshot) tetap bisa dibaca:
1. Pasang paket bahasa: `apt-get install -y tesseract-ocr-ind tesseract-ocr-chi-sim`
   (default hanya eng terpasang; ind+chi_sim untuk teks Indonesia/Mandarin).
2. Script siap pakai: `/root/.hermes/scripts/ocr_fallback.py`
   (preprocessing: upscale 2x LANCZOS + grayscale + kontras; coba `ind+eng` →
   `chi_sim` → `eng`; pilih hasil terpanjang). Contoh peningkatan akurasi:
   "Hala ini tesO0R 1231" (tesseract polos) → "Halo ini tesOCR 123!" (dengan
   preprocessing + ind+eng).
3. Panggil: `python3 /root/.hermes/scripts/ocr_fallback.py <path_gambar>`.

## Aturan anti-relay (wajib di system prompt, bukan cuma memori)
Tambah ke `agent.platform_hints.whatsapp.append` (lihat
references/platform-hints-persona-injection.md):
- Kalau deskripsi gambar di konteks tidak berguna → coba OCR dulu via terminal.
- Kalau tetap gagal → JANGAN PERNAH meneruskan pesan error/apologi sistem
  analisis gambar (termasuk teks berbahasa asing), jangan sebut nama tool
  internal (vision_analyze), balas natural: "Maaf, aku nggak bisa lihat
  gambarnya. Coba kirim ulang ya 🙏".
Sinkronkan juga ke file panduan identitas (~/.hermes/scripts/wa_bot_identity.md)
dan memori (entry ringkas + contoh).

## Catatan
- Quota Gemini free tier reset per hari (sekitar tengah malam waktu Pasifik);
  alternatif permanen: key Gemini baru gratis dari AI Studio, atau provider
  vision lain (OpenRouter/DeepInfra/Nous) yang dikonfigurasi di auxiliary.vision.*.
- Jangan pernah menulis "vision rusak" sebagai fakta permanen; ini state
  sementara provider yang bisa pulih — yang durable adalah pola diagnosa +
  fallback OCR + aturan anti-relay.
