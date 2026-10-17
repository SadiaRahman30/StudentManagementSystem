from selenium import webdriver
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

    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)

    if driver.title == "Student Management System - Login":
        print("TEST PASSED: Page title is correct.")
    else:
        print("TEST FAILED: Page title mismatch.")
        sys.exit(1)

    print("\nTest-1 Login Page Load Test: COMPLETED")

except Exception as e:
    print("Error:", e)
    sys.exit(1)
finally:
    driver.quit()
    print("Browser closed.")
