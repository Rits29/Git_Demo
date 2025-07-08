from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#https://rahulshettyacademy.com/angularpractice/
#https://rahulshettyacademy.com/seleniumPractise/#/
time.sleep(2)
driver.maximize_window()
print("Website opened successfully")

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@class='search-button']").click()
time.sleep(4)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
n = len(products)
print("Number of products found:", n)
assert n > 0

for i in range(n):
#for product in products:
    products[i].find_element(By.XPATH, "div/button").click() # don't add // in front of div/button here as we are chaining the elements
    print("Clicked on Add button for product.")
time.sleep(4)

driver.quit()
print("Browser closed successfully")

# This code opens a website, searches for products, and verifies that at least one product is found.
# Introduce Chaining web elements, In this case, we are chaining the find_element method to find the first product 
# and click it. products has the scope of the selected elements and we can chain the click method directly to products
# in place of driver. Driver has access to all the elements on the page, but products is a list of elements that 
# match the specified criteria. So we add the remaining part of the code to click on Add button.