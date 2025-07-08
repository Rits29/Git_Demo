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

#In this wesite on page loading the above text box is displayed and once we click on Hide it should get hidden. 
#Thats the validation we are doing here.


assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed() 
# Checks if Element is displayed on the page or not.
driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
# Click on the Hide button to hide the text box
time.sleep(2)  # Wait for the action to complete
print("Clicked on Hide button")
# After clicking Hide, the text box should not be displayed
# Validate that the text box is no longer displayed
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed() #This is called negations.

driver.quit()
print("Browser closed successfully")
# This code opens a website, checks if a text box is displayed, clicks a button to hide it, and then verifies that the text box is no longer displayed.
# It uses Selenium to automate the browser actions and chromedriver_autoinstaller to ensure the correct version of ChromeDriver is used.
# The script includes assertions to validate the visibility of the text box before and after the button click.