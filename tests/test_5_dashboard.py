from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, os, sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
register_url = "file:///" + os.path.join(project_dir, "register.html").replace("\\", "/")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get(register_url)
    time.sleep(1)

    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    print("Page Title:", driver.title)

    driver.find_element(By.ID, "name").send_keys("Test Student")
    driver.find_element(By.ID, "email").send_keys("test@student.com")
    driver.find_element(By.ID, "password").send_keys("test123")
    driver.find_element(By.ID, "confirmPassword").send_keys("test123")
    print("Filled registration form.")

    driver.find_element(By.ID, "registerBtn").click()
    time.sleep(1)

    success_msg = driver.find_element(By.ID, "successMessage")
    if success_msg.is_displayed():
        print("TEST PASSED: Registration successful -", success_msg.text)
    else:
        print("TEST FAILED: Registration success message not displayed.")
        sys.exit(1)

    print("\nTest-5 Register Page Test: COMPLETED")

except Exception as e:
    print("Error:", e)
    sys.exit(1)
finally:
    driver.quit()
    print("Browser closed.")
