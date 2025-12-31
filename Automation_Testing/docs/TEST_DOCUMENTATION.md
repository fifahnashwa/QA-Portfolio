# Dokumentasi Testing - Login Functionality

## Test Overview

### Deskripsi
Dokumen ini berisi hasil testing terhadap fungsi login pada aplikasi demo Applitools (https://demo.applitools.com/). Testing dilakukan menggunakan automation testing dengan framework Selenium WebDriver dan Pytest.

### Informasi Testing
- **Fitur yang Diuji**: Login Functionality
- **Jenis Testing**: Functional Testing, Negative Testing, UI Testing
- **Metode**: Automation Testing
- **Framework**: Selenium WebDriver + Pytest
- **Browser**: Google Chrome (latest version)
- **Bulan Eksekusi**: Desember 2025
- **Tester**: T. Afifah Nashwa

---

## Test Scope

### Yang Termasuk dalam Testing
- Login dengan kredensial valid (positive case)
- Login dengan kredensial invalid (negative case)
- Validasi field kosong (empty field validation)
- Validasi elemen UI (checkbox, button)
- Perilaku aplikasi terhadap berbagai input user

---

## Test Case Summary

### Tabel Test Cases

| ID | Skenario Test | Langkah Pengujian | Expected Result | Actual Result | Status | Priority |
|----|---------------|-------------------|-----------------|---------------|--------|----------|
| TC-001 | Login dengan kredensial valid | 1. Buka halaman login<br>2. Input username: "admin"<br>3. Input password: "password"<br>4. Klik tombol Sign In | User berhasil login dan diarahkan ke halaman app | User berhasil login, URL berubah ke app.html | PASS | High |
| TC-002 | Login dengan username invalid | 1. Buka halaman login<br>2. Input username: "invaliduser"<br>3. Input password: "password"<br>4. Klik tombol Sign In | Muncul error message, user tidak dapat login | Tidak muncul error message, user tetap bisa login | FAIL | High |
| TC-003 | Login dengan password invalid | 1. Buka halaman login<br>2. Input username: "admin"<br>3. Input password: "wrongpassword"<br>4. Klik tombol Sign In | Muncul error message, user tidak dapat login | Tidak muncul error message, user tetap bisa login | FAIL | High |
| TC-004 | Login dengan field kosong | 1. Buka halaman login<br>2. Tidak input apapun<br>3. Klik tombol Sign In | Login ditolak, user tetap di halaman login | User berhasil login meskipun field kosong | FAIL | Medium |
| TC-005 | Login dengan username kosong | 1. Buka halaman login<br>2. Kosongkan username<br>3. Input password: "password"<br>4. Klik tombol Sign In | Login ditolak, validasi username wajib diisi | User berhasil login meskipun username kosong | FAIL | Medium |
| TC-006 | Login dengan password kosong | 1. Buka halaman login<br>2. Input username: "admin"<br>3. Kosongkan password<br>4. Klik tombol Sign In | Login ditolak, validasi password wajib diisi | User berhasil login meskipun password kosong | FAIL | Medium |
| TC-007 | Fungsi Remember Me checkbox | 1. Buka halaman login<br>2. Cari checkbox "Remember Me"<br>3. Klik checkbox | Checkbox dapat diklik dan berubah state | Checkbox berfungsi dengan baik | PASS | Low |
| TC-008 | Status tombol Sign In | 1. Buka halaman login<br>2. Periksa tombol Sign In | Tombol Sign In selalu aktif dan dapat diklik | Tombol Sign In aktif dan dapat diklik | PASS | Low |

---

## Test Execution Summary

### Ringkasan Hasil

| Metrik | Jumlah | Persentase |
|--------|--------|------------|
| **Total Test Cases** | 8 | 100% |
| **Passed** | 3 | 37.5% |
| **Failed** | 5 | 62.5% |
| **Blocked** | 0 | 0% |
| **Not Executed** | 0 | 0% |

### Breakdown per Kategori

| Kategori Testing | Passed | Failed | Total |
|------------------|--------|--------|-------|
| Positive Test | 1 | 0 | 1 |
| Negative Test | 0 | 2 | 2 |
| Validation Test | 0 | 3 | 3 |
| UI Test | 2 | 0 | 2 |

### Hasil Eksekusi
```
========================================================== test session starts ==========================================================
platform win32 -- Python 3.10.6, pytest-9.0.2, pluggy-1.6.0
collected 8 items

automation/test_login.py::TestLogin::test_valid_login PASSED                    [ 12%]
automation/test_login.py::TestLogin::test_invalid_username FAILED               [ 25%]
automation/test_login.py::TestLogin::test_invalid_password FAILED               [ 37%]
automation/test_login.py::TestLogin::test_empty_credentials FAILED              [ 50%]
automation/test_login.py::TestLogin::test_empty_username_only FAILED            [ 62%]
automation/test_login.py::TestLogin::test_empty_password_only FAILED            [ 75%]
automation/test_login.py::TestLogin::test_remember_me_checkbox PASSED           [ 87%]
automation/test_login.py::TestLogin::test_login_button_enabled PASSED           [100%]

================================================ 5 failed, 3 passed in 67.26s =================================================
```

---

## Validation Gaps Identified During Login Testing

Selama proses testing, beberapa celah validasi input teridentifikasi. Perilaku-perilaku ini dapat berdampak pada pengalaman pengguna dan sebaiknya diperbaiki untuk memberikan feedback yang lebih jelas saat login gagal.

### Finding 1: Tidak Ada Error Message untuk Invalid Credentials

**Test Case Terkait**: TC-002, TC-003  
**Severity**: 🟡 Medium  
**Priority**: High

**Deskripsi**:
Ketika user memasukkan username atau password yang salah, aplikasi tidak menampilkan pesan error apapun. Aplikasi tetap mengizinkan proses login berlanjut tanpa memberikan informasi kepada user bahwa kredensial yang dimasukkan tidak valid.

**Perilaku yang Teramati**:
- Input: username invalid + password valid → Tidak ada error message
- Input: username valid + password invalid → Tidak ada error message
- Aplikasi menunggu 10 detik (timeout) sebelum test dinyatakan gagal

**Dampak**:
- User tidak mendapat feedback yang jelas
- Dapat menyebabkan kebingungan pada user
- Pengalaman pengguna (UX) kurang optimal

**Rekomendasi**:
Menambahkan error message yang jelas seperti "Username atau password salah. Silakan coba lagi." untuk membantu user memahami mengapa login gagal.

---

### Finding 2: Aplikasi Mengizinkan Login dengan Field Kosong

**Test Case Terkait**: TC-004, TC-005, TC-006  
**Severity**: 🟡 Medium  
**Priority**: Medium

**Deskripsi**:
Aplikasi tidak melakukan validasi input pada saat tombol Sign In diklik. User dapat login bahkan ketika:
- Kedua field (username dan password) kosong
- Hanya username yang diisi
- Hanya password yang diisi

**Perilaku yang Teramati**:
- Tombol Sign In dapat diklik meskipun field kosong
- User berhasil diarahkan ke halaman app.html meskipun tidak memasukkan kredensial
- Tidak ada validasi client-side maupun feedback visual

**Dampak**:
- Celah validasi yang dapat dieksploitasi
- Dapat mempengaruhi keamanan aplikasi
- User experience yang tidak konsisten

**Rekomendasi**:
1. Menambahkan validasi client-side:
   - Disable tombol Sign In jika field kosong
   - Tampilkan pesan "Username dan password wajib diisi"
2. Menambahkan validasi server-side sebagai lapisan keamanan tambahan
3. Memberikan visual indicator (contoh: border merah) pada field yang kosong

---

## Catatan Tambahan

### Keterbatasan Testing
1. **Environment Terbatas**: Testing hanya dilakukan pada environment Chrome browser Windows. Belum diuji pada browser lain (Firefox, Safari, Edge) atau sistem operasi lain.

2. **Demo Application**: Website yang diuji adalah aplikasi demo untuk tujuan pembelajaran testing.

### Asumsi Testing
- Username valid yang digunakan: "admin"
- Password valid yang digunakan: "password"
- Aplikasi diasumsikan harus menolak login dengan kredensial invalid atau field kosong
- Error message diasumsikan sebagai best practice untuk user experience

### Potential Improvements untuk Automation Suite
1. **Menambahkan Test Cases**:
   - Test untuk special characters pada username/password
   - Test untuk maksimal panjang input
   - Test untuk copy-paste kredensial

2. **Reporting Enhancement**:
   - Implementasi HTML report dengan screenshot
   - Integrasi dengan CI/CD pipeline
   - Video recording untuk failed tests

3. **Framework Improvement**:
   - Menambahkan Page Object Model (POM) pattern
   - Implementasi data-driven testing
   - Menambahkan parallel execution

### Kesimpulan
Dari 8 test case yang dijalankan, 3 test berhasil (37.5%) dan 5 test gagal (62.5%). Test yang gagal bukan karena masalah pada automation script, melainkan karena aplikasi memiliki celah validasi yang teridentifikasi. Findings ini dapat dijadikan masukan untuk perbaikan aplikasi guna meningkatkan keamanan dan pengalaman pengguna.

---

**Dokumen ini dibuat untuk keperluan portfolio testing dan demonstrasi kemampuan automation testing menggunakan Selenium WebDriver dan Pytest.**
