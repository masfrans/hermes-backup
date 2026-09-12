---
name: testimoni-course-analisis
description: "Analisis testimoni course jadi JSON terstruktur (CSAT)."
version: 1.0.0
platforms: [linux]
---

# Analisis Testimoni Course (CSAT)

Mengubah teks testimoni peserta yang subjektif/tidak terstruktur menjadi data
objektif terstruktur JSON untuk evaluasi kualitas course online.

## Trigger

- User mengirim testimoni peserta course/kelas/webinar dan minta dianalisis
- Evaluasi CSAT BelajarLagi / free class / bootcamp
- User paste teks testimoni (satu atau banyak) lalu minta breakdown

## Aturan Analisis

1. **Berbasis bukti**: hanya simpulkan dari isi testimoni, tanpa asumsi
2. **FACT / OPINION / INFERENCE / NOT_MENTIONED**: tandai jenis tiap info;
   prioritaskan FACT & OPINION; INFERENCE hanya jika perlu & ditandai
3. **Jangan mengarang**: jika tidak ada di teks → NOT_MENTIONED
4. **Pertahankan konteks**: jangan pecah kalimat sampai maknanya berubah
   (contoh: "materi bagus tapi waktu singkat" = material positif + durasi negatif)
5. **Pisahkan positif & negatif**: satu testimoni bisa MIXED

## Dimensi yang Dianalisis

- **A. Overall Experience**: VERY_POSITIVE/POSITIVE/MIXED/NEGATIVE/VERY_NEGATIVE/NOT_MENTIONED + alasan
- **B. Course Material**: relevansi, kejelasan, struktur, kedalaman, contoh, kelengkapan
- **C. Instructor/Facilitator**: kejelasan, penguasaan, menjawab pertanyaan, cara mengajar, interaksi
- **D. Online Class Execution**: kelancaran, ketepatan waktu, struktur sesi, koordinasi
- **E. Technology/Platform**: platform, koneksi, audio/video, recording, kendala teknis
- **F. Interaction & Engagement**: HIGH/MEDIUM/LOW/NOT_MENTIONED (diskusi, Q&A, breakout, polling, games)
- **G. Duration & Time Management**: cukup/panjang/singkat, pacing, waktu praktik
- **H. Assignments/Practice**: tugas, latihan, relevansi, kesulitan, feedback
- **I. Positive Points**: hal yang diapresiasi (spesifik, bukan "kelasnya bagus")
- **J. Pain Points**: masalah yang disebutkan (jangan membuat masalah baru)
- **K. Improvement Suggestions**: saran eksplisit (pisahkan dari masalah)
- **L. Perceived Impact**: KNOWLEDGE/SKILL/CONFIDENCE/PRACTICAL_APPLICATION/WORK_PERFORMANCE/CAREER/PROBLEM_SOLVING/OTHER/NOT_MENTIONED

## Sentiment per Dimensi

POSITIVE / NEGATIVE / MIXED / NEUTRAL / NOT_MENTIONED - level dimensi, bukan hanya keseluruhan.

## Evidence & Confidence

- **Evidence**: kutipan pendek LANGSUNG dari teks (bukan parafrase)
- **Confidence**: HIGH (eksplisit) / MEDIUM (indikasi kuat) / LOW (interpretasi lemah)
- NOT_MENTIONED tidak butuh confidence

## Output JSON

Struktur lengkap ada di prompt template (file `templates/prompt.md`). Field inti:
overall, course_material, instructor, online_execution, technology_platform,
interaction_engagement, duration_time_management, assignments_practice,
positive_points, pain_points, improvement_suggestions, perceived_impact,
objective_facts, key_insight, missing_information.

## Aturan Penting Lain

- **objective_facts**: hanya info yang bisa jadi data evaluasi (durasi, jumlah sesi,
  platform, dll). Jangan ubah opini jadi fakta ("instruktur sangat bagus" =
  participant_opinion, bukan instructor_quality=excellent)
- **key_insight**: 2-3 kalimat, objektif, spesifik, tanpa info baru
- **Testimoni sangat pendek** ("Keren banget!"): jangan mengarang; overall
  sentiment dari bukti minim, isi missing_information dengan dimensi yang tidak ada
- **Bahasa Indonesia profesional**: objektif, ringkas, tanpa kata marketing
  (luar biasa/sempurna/pasti) kecuali kutipan langsung peserta

## Pitfall

- Jangan simpulkan "instruktur kompeten" hanya karena kelas menyenangkan
- Jangan simpulkan dampak (nilai naik, skill naik) tanpa disebutkan peserta
- Satu testimoni bisa punya sentimen beda per dimensi - jangan dipaksa satu label
