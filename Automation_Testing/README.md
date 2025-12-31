# Automation Testing - Login Functionality

## 📖 Deskripsi
Repository ini berisi automation testing untuk fungsi login menggunakan Selenium WebDriver dengan Python dan Pytest framework. Testing dilakukan pada website demo Applitools untuk mendemonstrasikan kemampuan automation testing dan identifikasi celah validasi.

**Website Under Test**: [Applitools Demo](https://demo.applitools.com/)

---

## 🎯 Cakupan Testing
- ✅ Login dengan kredensial valid (positive case)
- ✅ Login dengan kredensial invalid (negative case)
- ✅ Validasi input kosong (empty field validation)
- ✅ Validasi elemen UI (checkbox, button)
- ✅ Identifikasi celah validasi

---

## 📋 Test Cases

| ID | Test Case | Tipe | Priority | Status |
|----|-----------|------|----------|--------|
| TC-001 | Login dengan kredensial valid | Positive | High | ✅ PASS |
| TC-002 | Login dengan username invalid | Negative | High | ❌ FAIL* |
| TC-003 | Login dengan password invalid | Negative | High | ❌ FAIL* |
| TC-004 | Login dengan field kosong | Negative | Medium | ❌ FAIL* |
| TC-005 | Login dengan username kosong | Boundary | Medium | ❌ FAIL* |
| TC-006 | Login dengan password kosong | Boundary | Medium | ❌ FAIL* |
| TC-007 | Fungsi Remember Me checkbox | UI | Low | ✅ PASS |
| TC-008 | Status tombol login | UI | Low | ✅ PASS |

**Total**: 8 test cases | **Passed**: 3 (37.5%) | **Failed**: 5 (62.5%)

*Test yang failed menunjukkan celah validasi yang teridentifikasi pada aplikasi. Detail lengkap ada di [dokumentasi testing](docs/TEST_DOCUMENTATION.md).

---

## 🛠️ Tech Stack
- **Python** 3.10+
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **WebDriver Manager** - Automatic driver management

---

## 📁 Struktur Project
```
automation-login-testing/
├── venv/                           # Virtual environment (tidak di-upload ke GitHub)
├── automation/
│   └── test_login.py              # Test suite dengan 8 test cases
├── docs/
│   └── TEST_DOCUMENTATION.md      # Dokumentasi testing lengkap
├── requirements.txt                # Dependencies Python
├── .gitignore                     # File yang diabaikan Git
└── README.md                      # Dokumentasi project (file ini)
```

### Penjelasan File:
- **`automation/test_login.py`**: Berisi semua test cases untuk fungsi login menggunakan Pytest framework dengan proper assertions dan WebDriverWait
- **`docs/TEST_DOCUMENTATION.md`**: Dokumentasi lengkap hasil testing termasuk test cases, findings, dan rekomendasi
- **`requirements.txt`**: Daftar package Python yang diperlukan
- **`.gitignore`**: Konfigurasi file yang tidak perlu di-upload ke repository

---

## 🚀 Setup & Instalasi

### Prerequisites:
- Python 3.7 atau lebih tinggi
- pip (Python package manager)
- Google Chrome browser

### Langkah Instalasi:

#### 1. Clone Repository
```bash
git clone <url-repository-anda>
cd automation-login-testing
```

#### 2. Buat Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Tanda berhasil: Command prompt Anda akan menampilkan `(venv)` di awal.

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Ini akan menginstall:
- selenium
- webdriver-manager
- pytest

---

## ▶️ Cara Menjalankan Test

### Menjalankan Semua Test:
```bash
pytest automation/test_login.py -v
```

### Menjalankan dengan Output Detail:
```bash
pytest automation/test_login.py -v -s
```

### Menjalankan Test Case Spesifik:
```bash
pytest automation/test_login.py::TestLogin::test_valid_login -v
```

### Generate HTML Report:
```bash
pytest automation/test_login.py --html=report.html
```

---

## 📊 Hasil Testing
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

**Catatan**: Test yang failed mengidentifikasi celah validasi pada aplikasi. Ini menunjukkan kemampuan testing dalam menemukan potential issues. Lihat [dokumentasi lengkap](docs/TEST_DOCUMENTATION.md) untuk detail findings.

---

## 🔍 Key Features

✅ **Professional test structure** menggunakan Pytest framework  
✅ **Explicit waits** dengan WebDriverWait (tidak menggunakan time.sleep)  
✅ **Proper assertions** untuk semua test cases  
✅ **Clean code** dengan penamaan test case yang jelas  
✅ **Comprehensive coverage** untuk login functionality  
✅ **Dokumentasi lengkap** dalam Bahasa Indonesia

---

## 📝 Pendekatan Testing

- **Framework**: Pytest
- **Wait Strategy**: Explicit waits menggunakan WebDriverWait
- **Assertion**: Built-in Python assert dengan error message yang jelas
- **Browser**: Chrome (dikelola otomatis oleh webdriver-manager)
- **Test Design**: Independent test cases dengan setup/teardown fixtures

---

## 🔄 Deactivate Virtual Environment

Setelah selesai testing, keluar dari virtual environment:
```bash
deactivate
```

---

## 📌 Catatan Penting

- Test berjalan pada Chrome browser secara default
- Setiap test case bersifat independen (tidak ada dependency antar test)
- Browser otomatis dibersihkan setelah setiap test
- WebDriver dikelola otomatis (tidak perlu download driver manual)
- Untuk mengaktifkan virtual environment setiap kali membuka terminal baru, jalankan command activate seperti di langkah instalasi

---

## 📄 Dokumentasi Tambahan

Untuk dokumentasi testing lengkap termasuk test cases detail, findings, dan rekomendasi, silakan baca:
- 📘 [Dokumentasi Testing Lengkap](docs/TEST_DOCUMENTATION.md)

---

## 👨‍💻 Author

**[Nama Anda]**  
QA Testing Portfolio | [LinkedIn](link-anda) | [Email](email-anda)

---

## 📫 Contact & Feedback

Jika ada pertanyaan atau saran terkait project ini, silakan hubungi melalui:
- Email: [email-anda]
- LinkedIn: [linkedin-anda]

---

**Project ini dibuat untuk keperluan portfolio dan demonstrasi kemampuan automation testing.**
```

---

## 📁 **3. `.gitignore`**
```
# Virtual Environment
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Pytest
.pytest_cache/
.coverage
htmlcov/
*.html

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Test outputs
screenshots/
reports/
```

---

## 📁 **4. `requirements.txt`**
```
selenium
webdriver-manager
pytest