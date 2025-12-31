
# Functional Testing: User Registration Feature

> Dokumentasi ini menyajikan hasil functional testing secara manual pada fitur registrasi pengguna, mencakup test case, execution results, dan defect findings.

---

## Test Information

**Feature:** User Registration (Buyer)  
**Approach:** Functional Testing - Manual  
**Techniques:** Equivalence Partitioning, Boundary Value Analysis  
**Period:** Juni 2025  
**Environment:** Android API 33, Samsung A32 4G

---

## Test Objective

Memvalidasi bahwa fitur registrasi menangani berbagai input scenarios dengan benar, termasuk validasi field kosong, format email, dan panjang password.

---

## Acceptance Criteria

**Email Requirements:**
- Tidak boleh kosong
- Harus format email valid
- Tidak boleh duplikasi

**Password Requirements:**
- Tidak boleh kosong
- Minimal 6 karakter

**Success Criteria:**
- User tersimpan di authentication system
- User data tersimpan di database
- Redirect ke main screen

---

## Test Cases

| No | Scenario | Input | Expected | Actual | Status | Bug |
|----|----------|-------|----------|--------|--------|-----|
| 1 | Valid input | Valid email & password | Success toast + redirect | Toast tidak jelas | FAIL | BUG-003 |
| 2 | Empty email | Email: kosong | Error message | Sesuai expected | PASS | - |
| 3 | Empty password | Password: kosong | Error message | Sesuai expected | PASS | - |
| 4 | Both empty | Kedua field kosong | Error untuk semua field | Hanya 1 error | FAIL | BUG-001 |
| 5 | Invalid format | Email tanpa domain | Format error | Sesuai expected | PASS | - |
| 6 | Special chars | Email dengan `%%` | Format error | Registration sukses | FAIL | BUG-002 |
| 7 | Short password | Password < 6 chars | Error message | Sesuai expected | PASS | - |
| 8 | Password symbols | Password dengan simbol | Success | Sesuai expected | PASS | - |
| 9 | Password numbers | Password dengan angka | Success | Sesuai expected | PASS | - |
| 10 | Duplicate email | Email sudah terdaftar | Error: already exists | Sesuai expected | PASS | - |
| 11 | Boundary test | Password = 6 chars | Success | Sesuai expected | PASS | - |
| 12 | Missing @ | Email tanpa @ | Format error | Sesuai expected | PASS | - |

---

## Test Results

**Summary:**
- Total: 12 test cases
- Passed: 8 (66.67%)
- Failed: 4 (33.33%)
- Defects: 3 found

**By Category:**

| Category | Cases | Passed | Failed |
|----------|-------|--------|--------|
| Valid Input | 4 | 3 | 1 |
| Empty Fields | 3 | 2 | 1 |
| Format | 3 | 2 | 1 |
| Password | 2 | 2 | 0 |

---

## Defects Found

### BUG-001: Multiple Field Validation
**Severity:** Major

**Issue:** Ketika beberapa field invalid bersamaan, hanya error pertama yang ditampilkan.

**Impact:** User harus fix error satu per satu, menurunkan user experience.

**Root Cause:** Validasi berhenti pada pengecekan pertama. Error pada field lain tidak pernah dicek.

**Recommendation:** Implementasikan validasi yang mengecek semua field sebelum menentukan form valid/invalid.

---

### BUG-002: Email Format Not Validated
**Severity:** Major

**Issue:** Email dengan format invalid (misal: `test%%@gmail.com`) berhasil tersimpan di system.

**Impact:** 
- Email invalid tersimpan di database
- Fitur email-based (reset password, notification) tidak akan berfungsi
- Data integrity issue

**Root Cause:** Tidak ada validasi format email di client-side sebelum submit ke backend.

**Recommendation:** Tambahkan validasi format email di client-side menggunakan standard email pattern validation.

---

### BUG-003: Success Feedback Not Clear
**Severity:** Minor

**Issue:** Toast message "Registration successful" tidak terlihat jelas karena screen langsung redirect.

**Impact:** User tidak mendapat konfirmasi yang jelas bahwa registrasi berhasil.

**Root Cause:** Screen langsung berpindah sebelum toast sempat ditampilkan dengan jelas.

**Recommendation:** Tambahkan delay sebelum redirect atau gunakan dialog confirmation yang lebih prominent.

---

## Observations

**Strengths:**
- Password length validation bekerja dengan baik
- Backend integration berfungsi
- Duplicate email handling sudah benar

**Improvement Areas:**
- Form validation perlu show all errors simultaneously
- Client-side email format validation diperlukan
- User feedback untuk success case dapat ditingkatkan

---

## Conclusion

Fitur registrasi memiliki pass rate 66.67% dengan 3 defects ditemukan. Fungsionalitas dasar bekerja, namun ada area improvement penting pada input validation dan user feedback.

**Scope Note:** Testing dilakukan pada fitur registrasi saja dan tidak mencakup flow lengkap aplikasi.

---

**Period:** Juni 2025
