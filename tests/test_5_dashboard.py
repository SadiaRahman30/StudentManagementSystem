from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
register_url = "file:///" + os.path.join(project_dir, "register.html").replace("\\", "/")

driver = webdriver.Chrome()

try:
    driver.get(register_url)
    time.sleep(2)

    print("Page Title:", driver.title)

    driver.find_element(By.ID, "name").send_keys("Test Student")
    driver.find_element(By.ID, "email").send_keys("test@student.com")
    driver.find_element(By.ID, "password").send_keys("test123")
    driver.find_element(By.ID, "confirmPassword").send_keys("test123")
    print("Filled registration form.")

    driver.find_element(By.ID, "registerBtn").click()
    time.sleep(2)

    success_msg = driver.find_element(By.ID, "successMessage")
    if success_msg.is_displayed():
        print("TEST PASSED: Registration successful -", success_msg.text)

    print("\nTest-5 Register Page Test: COMPLETED")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
    print("Browser closed.")
