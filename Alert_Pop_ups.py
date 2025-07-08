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

#Selenium is used to automate the html css created websites its not capable of automating or handling any java or 
#  javascript popups or any such alert boxs. Hence To handle such popups selenium has provided Alert class in selenium
# Alert class is used to handle the alert popups in selenium

driver.find_element(By.NAME, "enter-name").send_keys("Ritvika Thakur")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert  
# Switch to the alert popup we can use 
print(alert.text)
assert "Ritvika Thakur" in alert.text  # Verify the text in the alert
print("Assert True")
alert.accept      # Accept the alert
#alert.dismiss()   # Dismiss the alert
driver.quit()  # Close the browser