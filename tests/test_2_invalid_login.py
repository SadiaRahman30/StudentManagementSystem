from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
login_url = "file:///" + os.path.join(project_dir, "index.html").replace("\\", "/")

driver = webdriver.Chrome()

try:
    driver.get(login_url)
    time.sleep(2)

    driver.find_element(By.ID, "email").send_keys("wrong@test.com")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "loginBtn").click()
    print("Entered invalid credentials and clicked Login.")

    time.sleep(2)

    error_msg = driver.find_element(By.ID, "errorMessage")
    if error_msg.is_displayed():
        print("TEST PASSED: Error message shown -", error_msg.text)
    else:
        print("TEST FAILED: No error message.")

    print("\nTest-2 Invalid Login Test: COMPLETED")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
    print("Browser closed.")
