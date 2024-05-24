from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (replace with the path to your WebDriver)
driver = webdriver.Chrome()

def wait_for_element(by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def sign_up(fullname,username, email, password, password_confirmation, ):
    driver.get("https://dev.trustline.sa/register-expert")
    wait_for_element(By.NAME, "floatingInputFullName").send_keys(fullname)
    driver.find_element(By.ID, "floatingInputFullName").send_keys(fullname)
    driver.find_element(By.ID, "floatingInputUsername").send_keys(username)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "floatingPasswordCustomPassword").send_keys(password)
    driver.find_element(By.ID, "floatingPasswordCustomRePassword").send_keys(password_confirmation)
    driver.find_element(By.XPATH, '//button[text()="Register"]').click()
    time.sleep(5)

def sign_in(email, password):
    driver.get("https://dev.trustline.sa/login")
    wait_for_element(By.ID, "floatingInputCustomEmailForExpert").send_keys(email)
    driver.find_element(By.ID, "floatingPasswordCustomPasswordForExpert").send_keys(password)
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    time.sleep(5)

def test_valid_signup():
    sign_up("John Doe", "johndoe@example.com", "SecurePassword123", "SecurePassword123", "555-555-5555", "Example Corp")
    assert "Dashboard" in driver.title  
def test_empty_signup():
    sign_up("", "", "", "", "", "")
    assert "This field is required" in driver.page_source  

def test_invalid_email_signup():
    sign_up("John Doe", "invalidemail", "SecurePassword123", "SecurePassword123", "555-555-5555", "Example Corp")
    assert "Enter a valid email address" in driver.page_source  
def test_password_mismatch_signup():
    sign_up("John Doe", "johndoe@example.com", "SecurePassword123", "DifferentPassword123", "555-555-5555", "Example Corp")
    assert "Passwords do not match" in driver.page_source  ch

def test_existing_email_signup():
    sign_up("John Doe", "existing@example.com", "SecurePassword123", "SecurePassword123", "555-555-5555", "Example Corp")
    assert "This email is already registered" in driver.page_source  

def test_valid_login():
    sign_in("johndoe@example.com", "SecurePassword123")
    assert "Dashboard" in driver.title  

def test_invalid_email_login():
    sign_in("invalidemail", "SecurePassword123")
    assert "Enter a valid email address" in driver.page_source  

def test_incorrect_password_login():
    sign_in("johndoe@example.com", "WrongPassword123")
    assert "Incorrect password" in driver.page_source  

def test_empty_login():
    sign_in("", "")
    assert "This field is required" in driver.page_source  

def test_non_existing_email_login():
    sign_in("nonexisting@example.com", "SecurePassword123")
    assert "This email is not registered" in driver.page_source  