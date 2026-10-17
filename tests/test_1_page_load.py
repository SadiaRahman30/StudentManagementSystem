from selenium import webdriver
import time, os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
login_url = "file:///" + os.path.join(project_dir, "index.html").replace("\\", "/")

driver = webdriver.Chrome()

try:
    driver.get(login_url)
    time.sleep(2)

    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)

    if driver.title == "Student Management System - Login":
        print("TEST PASSED: Page title is correct.")
    else:
        print("TEST FAILED: Page title mismatch.")

    print("\nTest-1 Login Page Load Test: COMPLETED")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
    print("Browser closed.")
