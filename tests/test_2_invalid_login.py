from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, os, sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
login_url = "file:///" + os.path.join(project_dir, "index.html").replace("\\", "/")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get(login_url)
    time.sleep(1)

    driver.find_element(By.ID, "email").send_keys("wrong@test.com")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "loginBtn").click()
    print("Entered invalid credentials and clicked Login.")

    time.sleep(1)

    error_msg = driver.find_element(By.ID, "errorMessage")
    if error_msg.is_displayed():
        print("TEST PASSED: Error message shown -", error_msg.text)
    else:
        print("TEST FAILED: No error message.")
        sys.exit(1)

    print("\nTest-2 Invalid Login Test: COMPLETED")

except Exception as e:
    print("Error:", e)
    sys.exit(1)
finally:
    driver.quit()
    print("Browser closed.")
