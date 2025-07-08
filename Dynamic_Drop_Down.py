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

# not req this click action - driver.find_elemnet(By.ID,"autocomplete").click()
driver.find_element(By.ID, "autocomplete").send_keys("Un")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,'li[class="ui-menu-item"] div')
n= len(countries)

for i in range(n):
    if countries[i].text == "United Arab Emirates":
        countries[i].click()
        print("Selected India from the dynamic dropdown")
        break

time.sleep(5)

#post we execute the script and if we try to read the text of the input using below code, it wont capture
#the text selected as this code is capable to read the text present on the webpage when the website loads.
#print(driver.find_element(By.ID, "autocomplete").text()) ---- nothing will be printed on terminal.
#When we need to capture the text post the text is supplied via automated script use the get_attribute("value") method
print("Selected country:", driver.find_element(By.ID, "autocomplete").get_attribute("value"))
#this way we can capture the sleceted text to perform any validations.
driver.quit()
print("Browser closed successfully")

# This code opens a website, interacts with a dynamic dropdown menu by sending keys and selecting an option, and then closes the browser.
# It uses Selenium to automate the browser actions and chromedriver_autoinstaller to ensure the correct version of ChromeDriver is used.
# The dynamic dropdown is handled by sending keys to an input field and selecting the desired option from the displayed list.
# Note: Ensure that the website and elements are accessible and that the necessary libraries are installed in your Python environment.
