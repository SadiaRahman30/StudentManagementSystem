from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
login_url = "file:///" + os.path.join(project_dir, "index.html").replace("\\", "/")

driver = webdriver.Chrome()

try:
    driver.get(login_url)
    time.sleep(1)

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

    time.sleep(4)

    print("Current Page:", driver.title)
    print("Current URL:", driver.current_url)

    if "dashboard" in driver.current_url:
        print("TEST PASSED: Login successful, dashboard is showing.")
        welcome = driver.find_element(By.ID, "navUserName")
        print("Welcome message:", welcome.text)

    print("\nTest-4 Valid Login in Selenium: COMPLETED")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
    print("Browser closed.")
