import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select    
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.maximize_window()
print("Website opened successfully")

driver.find_element(By.ID, "dropdown-class-example").click()
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option1")
print("Selected Option1 from the dropdown by visible text")
time.sleep(2)
dropdown.select_by_index(2)
print("Selected Option2 from the dropdown by index")
time.sleep(2)
dropdown.select_by_value("option3")
print("Selected Option3 from the dropdown by value")
time.sleep(2)
driver.quit()
print("Browser closed successfully")
# This code opens a website, interacts with a static dropdown menu, and then closes the browser.
# It uses Selenium to automate the browser actions and chromedriver_autoinstaller to ensure the correct version of ChromeDriver is used.

    

