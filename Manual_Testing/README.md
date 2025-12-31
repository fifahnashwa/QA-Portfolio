# KantinGKM – Dokumentasi Manual Software Testing

> Dokumentasi ini disusun sebagai bagian dari portfolio profesional untuk mendemonstrasikan praktik manual software testing yang terstruktur pada aplikasi mobile KantinGKM.

Pengujian dilakukan pada aplikasi yang dikembangkan dalam konteks proyek akademik, dengan dokumentasi disusun ulang untuk menunjukkan praktik manual software testing secara profesional.

Pengujian difokuskan pada dua pendekatan:
- **Functional Testing** (black-box) pada fitur registrasi
- **Path Analysis** (basis path testing) pada fungsi stock management

**Catatan:** Dokumentasi ini mencakup scope pengujian terbatas yang terdefinisi, bukan representasi QA lifecycle lengkap.

---

## Aplikasi yang Diuji

**KantinGKM** - Aplikasi pemesanan makanan berbasis mobile untuk Kantin Fakultas Ilmu Komputer (FILKOM)

**Link Repositori:** [github.com/dimassypp/KantinGKM](https://github.com/dimassypp/KantinGKM)

---

## Scope Pengujian

**Yang Diuji:**
- Fitur Registrasi Pengguna (functional testing)
- Logika Update Stock (path analysis)

**Tidak Diuji:**
- Fitur lain dalam aplikasi
- Performance, security, atau load testing
- Automated testing

---

## Struktur Dokumentasi

```
Manual_Testing/
├── README.md
├── functional_testing/
│   └── user-registration.md
├── path_analysis/
│   ├── stock-update-logic.md
│   └── flow-diagram.png
└── defects.md
```

---

## Hasil Pengujian

### Functional Testing
- **Test Case:** 12
- **Pass Rate:** 66.67%
- **Defect:** 3 ditemukan

📄 [Lihat detail](functional_testing/user-registration.md)

### Path Analysis
- **Cyclomatic Complexity:** 5
- **Path Coverage:** 100% (5/5 jalur)
- **Defect:** 0

📄 [Lihat detail](path_analysis/stock-update-logic.md)

---

## Defect Summary

| ID | Severity | Area |
|----|----------|------|
| BUG-001 | Major | Validasi form tidak menampilkan semua error |
| BUG-002 | Major | Format email tidak divalidasi |
| BUG-003 | Minor | Feedback sukses tidak jelas |

📄 [Lihat detail](defects.md)

---

## Testing Environment

- **Platform:** Android API 33
- **Device:** Emulator
- **Backend:** Firebase
- **Approach:** Manual Testing

**Tester:** T. Afifah Nashwa  
**Period:** Juni 2025

---

## Catatan
Observasi dan kesimpulan dibuat berdasarkan scope terbatas dan tidak merepresentasikan kualitas keseluruhan aplikasi.

---

**Terakhir Diperbarui:** Juni 2025
