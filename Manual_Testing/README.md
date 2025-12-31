# KantinGKM – Dokumentasi Manual Software Testing

Repositori ini berisi dokumentasi pengujian perangkat lunak secara manual pada aplikasi mobile KantinGKM. Pengujian difokuskan pada manual black-box testing dan manual white-box testing yang dilakukan pada fitur serta method tertentu dalam sistem.

Repositori ini disusun untuk menunjukkan:
- Penerapan praktik manual software testing secara terstruktur
- Penyusunan test case dan skenario uji yang jelas
- Analisis logika program menggunakan pendekatan white-box testing

Repositori ini tidak merepresentasikan keseluruhan siklus QA industri, melainkan dokumentasi pengujian yang dilakukan dalam lingkup terbatas dan terdefinisi.

---

## Gambaran Umum Aplikasi

KantinGKM merupakan aplikasi pemesanan makanan berbasis mobile yang dirancang untuk lingkungan Kantin Fakultas Ilmu Komputer (FILKOM). Aplikasi ini memungkinkan pengguna untuk melakukan registrasi, melihat menu, melakukan pemesanan, serta mendukung pengelolaan stok menu oleh penjual secara digital.

---

## Ruang Lingkup Pengujian

Pengujian yang dilakukan dalam repositori ini bersifat terbatas dan terfokus, dengan rincian sebagai berikut:

### Termasuk

- Manual black-box functional testing pada fitur yang berinteraksi langsung dengan pengguna
- Manual white-box testing (basis path testing) pada method tertentu di sisi backend
- Identifikasi dan dokumentasi defect serta perilaku sistem yang relevan

### Tidak Termasuk

- Automated testing
- Performance atau load testing
- Security testing
- End-to-end testing
- User Acceptance Testing (UAT)

Seluruh temuan dan kesimpulan dibuat berdasarkan ruang lingkup pengujian ini dan tidak digeneralisasi ke keseluruhan sistem.

---

## Sistem yang Diuji

| Aspek | Deskripsi |
|-------|-----------|
| Platform | Aplikasi Mobile Android |
| Backend | Firebase Realtime Database |
| Autentikasi | Firebase Authentication |
| Bahasa Pemrograman | Java |
| Jenis Pengujian | Manual Testing |

---

## Struktur Repositori
```
Manual_Testing/
│
├── README.md
│
├── white_box_testing/
│   ├── updateMenuStock.md
│   └── control-flow-graph.png
│
├── black_box_testing/
│   └── user-registration.md
│
└── defects.md
```

---

## White-box Testing

White-box testing dilakukan secara manual menggunakan metode Basis Path Testing pada method `updateMenuStock()`.

Aktivitas pengujian meliputi:
- Analisis kode sumber
- Penyusunan Control Flow Graph (CFG)
- Perhitungan Cyclomatic Complexity
- Identifikasi jalur eksekusi independen
- Penyusunan test case berdasarkan setiap jalur

Analisis difokuskan pada kebenaran logika dan potensi kegagalan, tanpa melakukan perubahan terhadap kode sumber.

**Dokumentasi lengkap tersedia pada:** [white_box_testing/updateMenuStock.md](white_box_testing/updateMenuStock.md)

---

## Black-box Testing

Black-box testing dilakukan secara manual pada fitur Registrasi Pengguna.

Pendekatan pengujian mencakup:
- Skenario input valid dan tidak valid
- Verifikasi respons sistem terhadap spesifikasi yang diharapkan
- Observasi terhadap mekanisme validasi dan pesan kesalahan

Hasil pengujian didokumentasikan secara jelas, termasuk status eksekusi dan catatan berdasarkan perilaku aktual sistem.

**Dokumentasi lengkap tersedia pada:** [black_box_testing/user-registration.md](black_box_testing/user-registration.md)

---

## Defect dan Temuan

Defect yang ditemukan selama pengujian didokumentasikan berdasarkan:
- Perilaku aktual sistem
- Perilaku yang diharapkan
- Dampak terhadap fungsionalitas

Tidak seluruh kasus gagal diklasifikasikan sebagai bug implementasi, karena beberapa dipengaruhi oleh batasan atau perilaku bawaan layanan Firebase.

**Lihat detail pada:** [defects.md](defects.md)

---

## Catatan

- Seluruh pengujian dilakukan secara manual
- Dokumentasi ini disusun dalam konteks pembelajaran dan portofolio
- Hasil pengujian terbatas pada fitur dan method yang diuji
- Kesimpulan tidak mewakili kualitas keseluruhan aplikasi

---

## Penulis

Dokumentasi Manual Software Testing
