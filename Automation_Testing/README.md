# Automation Testing – Login Functionality

Dokumentasi ini mencakup automation testing terhadap fungsi login pada aplikasi demo menggunakan Selenium WebDriver dan Pytest framework.

Pengujian difokuskan pada identifikasi celah validasi input dan verifikasi perilaku login functionality secara menyeluruh.

**Catatan:** Dokumentasi ini mencakup scope pengujian terbatas yang terdefinisi, bukan representasi QA lifecycle lengkap.

---

## Aplikasi yang Diuji

**Applitools Demo** - Aplikasi demo untuk praktik automation testing

Link Aplikasi: [demo.applitools.com](https://demo.applitools.com/)

---

## Scope Pengujian

### Yang Diuji:
* Login dengan kredensial valid (positive case)
* Login dengan kredensial invalid (negative case)
* Validasi input kosong (empty field validation)
* Elemen UI (checkbox, button state)
* Error message handling

---

## Struktur Dokumentasi
```
Automation_Testing/
├── README.md
├── automation/
│   └── test_login.py
├── docs/
│   └── TEST_DOCUMENTATION.md
└── requirements.txt
```

---

## Hasil Pengujian

### Test Case Summary

| Metrik | Jumlah | Persentase |
|--------|--------|------------|
| Total Test Cases | 8 | 100% |
| Passed | 3 | 37.5% |
| Failed | 5 | 62.5% |

📄 [Lihat detail lengkap](docs/TEST_DOCUMENTATION.md)

---

### Findings Summary

| ID | Severity | Area |
|----|----------|------|
| FIND-001 | Medium | Tidak ada error message untuk invalid credentials |
| FIND-002 | Medium | Aplikasi mengizinkan login dengan field kosong |

📄 [Lihat detail findings](docs/TEST_DOCUMENTATION.md#-validation-gaps-identified-during-login-testing)

---

## Testing Environment

* **Platform:** Web
* **Browser:** Google Chrome (latest version)
* **Framework:** Selenium WebDriver + Pytest
* **Language:** Python 3.10+
* **Approach:** Automation Testing

**Tester:** T. Afifah Nashwa
**Periode:** Desember 2025

---

## Setup dan Instalasi

### Prerequisites

* Python 3.7 atau lebih tinggi
* pip (Python package manager)
* Google Chrome browser

### Langkah Instalasi

**1. Clone repository**
```bash
git clone <url-repository>
cd QA-Portfolio/Automation_Testing
```

**2. Buat virtual environment (direkomendasikan)**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Menjalankan Test

### Perintah dasar:
```bash
pytest automation/test_login.py -v
```

### Opsi lainnya:

Dengan output detail:
```bash
pytest automation/test_login.py -v -s
```

Test case spesifik:
```bash
pytest automation/test_login.py::TestLogin::test_valid_login -v
```

Generate HTML report:
```bash
pytest automation/test_login.py --html=report.html
```

### Deactivate virtual environment:
```bash
deactivate
```

---

## Output Hasil Testing
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

**Catatan:** Test yang failed mengidentifikasi celah validasi pada aplikasi. Detail findings tersedia di [dokumentasi lengkap](docs/TEST_DOCUMENTATION.md).

---

## Dokumentasi Lengkap

Untuk detail test cases, findings, dan rekomendasi:

📘 [TEST_DOCUMENTATION.md](docs/TEST_DOCUMENTATION.md)

---
