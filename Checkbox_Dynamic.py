import time
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

# If id name and class is missing in the checkbox, we can use xpath to locate the checkbox using type attribute.
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
n = len(checkboxes)
print("Number of checkboxes found:", n)

for i in range(n):
    if checkboxes[i].get_attribute("value") == "option3":
        checkboxes[i].click()
        assert checkboxes[i].is_selected()
        # Here if we write retuen True error will be thrown because You should remove the 'return True' statement because
        #     'return' can only be used inside a function, and this code is not inside a function.
        #checkboxes has a method is_selected() to check if the checkbox is selected or not.
        # This will print True if the checkbox is selected, otherwise False.
        print("Clicked on checkbox")
        break

time.sleep(5)

driver.quit()
print("Browser closed successfully")
# This code opens a website, interacts with checkboxes by locating them using XPath, and then closes the browser.
# It uses Selenium to automate the browser actions and chromedriver_autoinstaller to ensure the correct version of ChromeDriver is used.
# The checkboxes are identified by their type attribute, and the script clicks on a specific checkbox based on its value.