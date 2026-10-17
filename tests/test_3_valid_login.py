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

    driver.execute_script("""
        localStorage.setItem('users', JSON.stringify([
            { name: 'Admin', email: 'admin@sms.com', password: 'admin123', role: 'Administrator' }
        ]));
    """)
    driver.refresh()
    time.sleep(1)

    driver.find_element(By.ID, "email").send_keys("admin@sms.com")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "loginBtn").click()
    print("Entered valid credentials and clicked Login.")

    time.sleep(0.5)

    success_msg = driver.find_element(By.ID, "successMessage")
    if success_msg.is_displayed():
        print("TEST PASSED: Success message shown -", success_msg.text)
    else:
        print("TEST FAILED: Success message not displayed.")
        sys.exit(1)

    time.sleep(2)

    if "dashboard" in driver.current_url:
        print("Redirected to Dashboard successfully.")
    else:
        print("TEST FAILED: Not redirected to dashboard.")
        sys.exit(1)

    print("\nTest-3 Valid Login Test: COMPLETED")

except Exception as e:
    print("Error:", e)
    sys.exit(1)
finally:
    driver.quit()
    print("Browser closed.")
