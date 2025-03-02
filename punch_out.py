import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load credentials from GitHub Secrets
USERNAME = os.getenv("FACTOHR_USERNAME")
PASSWORD = os.getenv("FACTOHR_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError("FACTOHR_USERNAME or FACTOHR_PASSWORD is missing!")

# Set up WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
driver = webdriver.Chrome(options=options)

# Open factoHR
driver.get("https://app2.factohr.com/tspl/Security/Login")

# Login
driver.find_element(By.ID, "txtUsername").send_keys(USERNAME)
driver.find_element(By.ID, "txtPassword").send_keys(PASSWORD)
driver.find_element(By.ID, "btnLogin").click()

# Wait for login to complete
time.sleep(15)

# Click Punch-Out
driver.find_element(By.ID, "Punch Out").click()

# Close browser
time.sleep(10)
driver.quit()
