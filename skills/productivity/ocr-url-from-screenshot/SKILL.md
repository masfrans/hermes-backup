---
name: ocr-url-from-screenshot
description: "Read URLs from screenshots via tesseract OCR cross-checking."
version: 2.0.0
platforms: [linux]
---

# OCR URL from Screenshot

Extract a URL from a user-sent screenshot using tesseract, with cross-checking because tesseract misreads small-font characters.

## When to use
- User sends an image containing a URL and asks "tulis ulang link/url ini"
- Vision model unavailable (GLM/DeepSeek text-only, Groq geo-blocked, Gemini quota habis/down)

## Cara TERCEPAT: script teroptimasi

Script siap pakai ada di **`/root/.hermes/scripts/ocr_optimized.py`**:

```bash
# Baca gambar biasa (bahasa Indonesia+Inggris otomatis)
python3 /root/.hermes/scripts/ocr_optimized.py /root/.hermes/cache/images/img_XXX.jpg

# Khusus cari URL/link (whitelist karakter URL)
python3 /root/.hermes/scripts/ocr_optimized.py /root/.hermes/cache/images/img_XXX.jpg --url

# Paksa bahasa / mode satu baris
python3 /root/.hermes/scripts/ocr_optimized.py img.jpg --lang ind
python3 /root/.hermes/scripts/ocr_optimized.py img.jpg --psm 7
```

Script otomatis: upscale 3x LANCZOS + grayscale + autocontrast, lalu cross-check 3 variasi (contrast/binary/sharpen) x 3 PSM (6, 3, 11), pilih hasil terbaik.

## Manual fallback (kalau script error)

1. **Locate the image** at `/root/.hermes/cache/images/img_*.jpg|png`.

2. **Run baseline OCR** (upscale 2x, autocontrast, PSM 6, bahasa ind+eng):
```bash
python3 -c "
from PIL import Image, ImageOps
img = Image.open('IMG_PATH').convert('L')
img = ImageOps.autocontrast(img)
img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
img.save('/tmp/ocr_base.png')
" && tesseract /tmp/ocr_base.png stdout -l ind+eng --psm 6
```

3. **Zoom into the URL ID zone** (10x, PSM 7) for the most reliable read:
```bash
python3 -c "
from PIL import Image
img = Image.open('IMG_PATH').convert('L')
w,h = img.size
c = img.crop((300, 0, 900, h))  # adjust x-range to the ID region
c = c.resize((c.width*10, c.height*10), Image.LANCZOS)
c.save('/tmp/ocr_zoom.png')
" && tesseract /tmp/ocr_zoom.png stdout --psm 7
```

4. **Cross-validate structure**:
   - Google Docs/Sheets IDs are exactly **44 chars** (base64url). If a read is 45 chars, one char is spurious (often a duplicated `0`).
   - `edit?gid=NNN#gid=NNN` duplication in OCR output is a rendering artifact; the real URL has one gid param.
   - Whitespace/`=`/`<`/`%6` prefixes are noise characters, not part of the URL.

## Known tesseract confusions (small fonts) — CRITICAL
These are verified mistakes from real sessions. When multiple reads disagree, prefer the character that makes the URL *valid* (44-char Google ID, plausible domain) and ask the user to confirm the ambiguous char if still unsure.

| Confusion | Example |
|---|---|
| `O` vs `0` (letter vs zero) | `VPOW` read, real was `VP0W` |
| `l` vs `T` vs `I` | `1Mol` read, real was `1MoT` |
| `g` vs `q` | `exag` read, real was `exaq` |
| `Z` vs `7` vs `2` | ambiguous in chat links |
| `8` vs `&` | `8PeWPM` vs `&PeWPM` |
| `o` vs `c` | URL tail chars |

Rule of thumb: if OCR gives a char from this confusion table, treat it as **unreliable** and report both candidates to the user, or ask them to confirm.

## Pitfalls
- Do NOT present a single OCR read as final without cross-checking at least 2 other thresholds/modes.
- Do NOT pad the URL with noise (`=`, `<3`, `%6`, quotes) that OCR adds at the start.
- The first read is often wrong in 1-2 chars; user confirmation is the ground truth.
- WhatsApp invite links: `chat.whatsapp.com/<22-char token>`, alphanumeric, mixed case.
- Binary (threshold) variant often FAILS on light-text-on-dark-background images — rely on contrast/sharpen variants instead.
- Indonesian text: always use `-l ind+eng`, default `eng` alone misreads Indonesian.

## Verification
After delivering the URL, ask the user to confirm it opens. If they say "masih eror", re-run with the zoom method and diff against the confusion table; ask the user for the correct version and use it to learn which char was misread.
