from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.maximize_window()
print("Website opened successfully")

radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
radiobuttons[2].click()  # Click on the third radio button as we know the number of radio button wont change.
assert radiobuttons[2].is_selected()  # Verify that the third radio button is selected
print("Clicked on the third radio button")
time.sleep(5)
driver.quit()
print("Browser closed successfully")
# This code opens a website, interacts with radio buttons by clicking on the third one, and then closes the browser.
# It uses Selenium to automate the browser actions and chromedriver_autoinstaller to ensure the correct version of ChromeDriver is used.
# The radio buttons are identified by their type attribute, and the script clicks on a specific radio button based on its index.
# Note: Ensure that the website and elements are accessible and that the necessary libraries are installed in your Python environment.