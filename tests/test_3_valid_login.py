from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
login_url = "file:///" + os.path.join(project_dir, "index.html").replace("\\", "/")

driver = webdriver.Chrome()

try:
    driver.get(login_url)
    time.sleep(2)

    driver.execute_script("""
        localStorage.setItem('users', JSON.stringify([
            { name: 'Admin', email: 'admin@sms.com', password: 'admin123' }
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

    time.sleep(2)

    if "dashboard" in driver.current_url:
        print("Redirected to Dashboard successfully.")

    print("\nTest-3 Valid Login Test: COMPLETED")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
    print("Browser closed.")
