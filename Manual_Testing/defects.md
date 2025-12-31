
# Defect Summary

> Dokumentasi defect yang ditemukan selama manual testing pada fitur registrasi pengguna KantinGKM.

**Testing Period:** Juni 2025  
**Scope:** User Registration Feature  
**Total Defects:** 3

---

## Overview

| Bug ID | Severity | Area | Status |
|--------|----------|------|--------|
| BUG-001 | Major | Form Validation | Open |
| BUG-002 | Major | Input Validation | Open |
| BUG-003 | Minor | User Feedback | Open |

**Distribution:** Major: 2 | Minor: 1

---

## BUG-001: Multiple Field Validation Issue

**Severity:** Major  
**Area:** Form Validation  
**Test Case:** TC-REG-004

### Description
Ketika multiple fields invalid secara bersamaan, sistem hanya menampilkan error message untuk field pertama. Error pada field lain tidak ditampilkan.

### Reproduction Steps
1. Buka registrasi screen
2. Kosongkan email field
3. Kosongkan password field
4. Klik register
5. Observe: Hanya email error yang muncul

### Expected vs Actual

**Expected:** Semua invalid fields menampilkan error message bersamaan
- Email: "Email cannot be empty"
- Password: "Password cannot be empty"

**Actual:** Hanya email error yang ditampilkan. Password error tidak muncul.

### Root Cause
Form validation menggunakan early-return pattern. Ketika first validation fails, fungsi langsung return tanpa mengecek field lainnya.

### Impact
User harus submit form multiple times untuk melihat semua validation errors. Menurunkan efficiency dan user experience.

### Recommendation
Ubah validation logic untuk mengecek semua fields terlebih dahulu. Kumpulkan semua errors sebelum menampilkan ke user.

---

## BUG-002: Email Format Not Validated

**Severity:** Major  
**Area:** Input Validation  
**Test Case:** TC-REG-006

### Description
System menerima email dengan format invalid (contoh: `test%%@gmail.com`) dan menyimpannya ke database. Format email ini tidak valid di real email systems.

### Reproduction Steps
1. Buka registrasi screen
2. Input email: `test%%@gmail.com`
3. Input password: `password123`
4. Klik register
5. Check database: Email tersimpan dengan format invalid

### Expected vs Actual

**Expected:** System menolak email format invalid
- Show error: "Invalid email format"
- Tidak save ke database

**Actual:** Registration success, email invalid tersimpan ke database

### Root Cause
Tidak ada client-side validation untuk email format. System hanya check apakah email empty atau tidak, kemudian langsung submit ke backend.

### Impact
- **Data Integrity:** Invalid email addresses stored in database
- **Feature Failure:** Email-dependent features (password reset, notifications) akan gagal
- **User Issues:** Users tidak bisa receive email communications

### Why This Matters
Standard email providers tidak accept karakter seperti `%` dalam email addresses. Users yang register dengan email invalid tidak akan bisa gunakan email-based features.

### Recommendation
Implement client-side email format validation sebelum submit ke backend. Gunakan standard email pattern validation untuk ensure format validity.

---

## BUG-003: Success Feedback Not Clear

**Severity:** Minor  
**Area:** User Feedback  
**Test Case:** TC-REG-001

### Description
Toast message "Registration successful" tidak terlihat dengan jelas karena application immediately redirects ke main screen.

### Reproduction Steps
1. Buka registrasi screen
2. Input valid email & password
3. Klik register
4. Observe: Toast appears very briefly atau tidak terlihat sama sekali
5. Screen langsung redirect

### Expected vs Actual

**Expected:** 
- Clear success message ditampilkan
- Message visible for 2-3 seconds
- Then redirect to main screen

**Actual:** 
- Toast appears very briefly
- Immediate redirect happens
- User may not see confirmation

### Root Cause
Screen transition happens immediately after toast is called, tidak memberi waktu bagi toast untuk properly display.

### Impact
Lack of clear feedback mengurangi user confidence. Users may be uncertain whether registration succeeded.

### Recommendation
Add delay before redirect atau gunakan more prominent confirmation (dialog) untuk ensure users see success feedback clearly.

---

## Priority Recommendations

Berdasarkan severity dan impact:

**High Priority:**
1. BUG-002 (Email Validation) - Data integrity issue
2. BUG-001 (Multiple Field Validation) - User experience issue

**Low Priority:**
3. BUG-003 (Success Feedback) - Minor UX polish

---

## Notes

**Testing Scope:** Defects documented berdasarkan testing pada user registration feature only. Tidak merepresentasikan quality dari keseluruhan application.

**Validation Approach:** Semua defects ditemukan melalui manual testing dan observasi actual system behavior.

---

**Tester:** T. Afifah Nashwa  
**Documentation Date:** Juni 2025
