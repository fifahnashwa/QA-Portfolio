import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()
    
    def test_valid_login(self):
        """TC-001: Verify successful login with valid credentials"""
        self.driver.get("https://demo.applitools.com/")
        
        # Input credentials
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("admin")
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("password")
        
        # Click sign in
        login_button = self.driver.find_element(By.ID, "log-in")
        login_button.click()
        
        # Assert: URL changed to app page
        self.wait.until(EC.url_contains("app.html"))
        assert "app.html" in self.driver.current_url, "Login failed - URL did not change"
    
    def test_invalid_username(self):
        """TC-002: Verify login fails with invalid username"""
        self.driver.get("https://demo.applitools.com/")
        
        self.driver.find_element(By.ID, "username").send_keys("invaliduser")
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "log-in").click()
        
        # Assert: Error message displayed
        error_message = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-warning"))
        )
        assert error_message.is_displayed(), "Error message not displayed"
        assert len(error_message.text) > 0, "Error message is empty"
    
    def test_invalid_password(self):
        """TC-003: Verify login fails with invalid password"""
        self.driver.get("https://demo.applitools.com/")
        
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("wrongpassword")
        self.driver.find_element(By.ID, "log-in").click()
        
        # Assert: Error message displayed
        error_message = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "alert-warning"))
        )
        assert error_message.is_displayed(), "Error message not displayed"
    
    def test_empty_credentials(self):
        """TC-004: Verify login fails with empty credentials"""
        self.driver.get("https://demo.applitools.com/")
        
        # Click login without entering credentials
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "log-in")))
        login_button.click()
        
        # Assert: Still on login page (URL should not change)
        current_url = self.driver.current_url
        assert "app.html" not in current_url, "Should not login with empty credentials"
        assert "demo.applitools.com" in current_url, "Should remain on login page"
    
    def test_empty_username_only(self):
        """TC-005: Verify login fails with empty username"""
        self.driver.get("https://demo.applitools.com/")
        
        # Enter password only
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "log-in").click()
        
        # Assert: Should not proceed to app
        current_url = self.driver.current_url
        assert "app.html" not in current_url, "Should not login without username"
    
    def test_empty_password_only(self):
        """TC-006: Verify login fails with empty password"""
        self.driver.get("https://demo.applitools.com/")
        
        # Enter username only
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "log-in").click()
        
        # Assert: Should not proceed to app
        current_url = self.driver.current_url
        assert "app.html" not in current_url, "Should not login without password"
    
    def test_remember_me_checkbox(self):
        """TC-007: Verify Remember Me checkbox is functional"""
        self.driver.get("https://demo.applitools.com/")
        
        # Locate and verify checkbox exists
        remember_checkbox = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".form-check-input"))
        )
        
        # Assert: Checkbox is clickable and changes state
        assert remember_checkbox.is_displayed(), "Remember Me checkbox not visible"
        initial_state = remember_checkbox.is_selected()
        remember_checkbox.click()
        assert remember_checkbox.is_selected() != initial_state, "Checkbox state did not change"
    
    def test_login_button_enabled(self):
        """TC-008: Verify login button is always enabled"""
        self.driver.get("https://demo.applitools.com/")
        
        login_button = self.wait.until(EC.presence_of_element_located((By.ID, "log-in")))
        
        # Assert: Button is enabled
        assert login_button.is_enabled(), "Login button should be enabled"
        assert login_button.is_displayed(), "Login button should be visible"