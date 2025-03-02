from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed

# Open factoHR
driver.get("https://app2.factohr.com/tspl/Security/Login")

# Login
driver.find_element(By.ID, "txtUsername").send_keys("A993")
driver.find_element(By.ID, "txtPassword").send_keys("Log@123#")
driver.find_element(By.ID, "btnLogin").click()

# Wait for login to complete
time.sleep(15)

# # Click Punch-In
driver.find_element(By.ID, "Punch In").click()

# Close browser
time.sleep(10)
driver.quit()
