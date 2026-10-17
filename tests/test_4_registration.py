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
            { name: 'Admin', email: 'admin@sms.com', password: 'admin123' }
        ]));
    """)
    driver.refresh()
    time.sleep(1)

    driver.find_element(By.ID, "email").send_keys("admin@sms.com")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "loginBtn").click()

    time.sleep(2.5)

    print("Current Page:", driver.title)
    print("Current URL:", driver.current_url)

    if "dashboard" in driver.current_url:
        print("TEST PASSED: Login successful, dashboard is showing.")
        welcome = driver.find_element(By.ID, "navUserName")
        print("Welcome message:", welcome.text)
    else:
        print("TEST FAILED: Not on dashboard.")
        sys.exit(1)

    print("\nTest-4 Valid Login in Selenium: COMPLETED")

except Exception as e:
    print("Error:", e)
    sys.exit(1)
finally:
    driver.quit()
    print("Browser closed.")
