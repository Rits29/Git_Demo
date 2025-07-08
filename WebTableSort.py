from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import chromedriver_autoinstaller
import time

#Click Col headers to sort items in a web table
#Collect the sorted in the veggieList. This is browser sorted list. 
#Apply sort on the veggieList. This will sort the list but it will be same as browser sorted list.
#Compare both lists. If they are same, then sorting is working fine.

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)
driver.maximize_window()
print("Website opened successfully")
driver.implicitly_wait(10)  # seconds
driver.find_element(By.XPATH, "//a[text()='Top Deals']").click()

handles = driver.window_handles
driver.switch_to.window(handles[1])  # Switch to the new window

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()  # Click on the first column header to sort
veggieList_addr = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")  # Get all items in the first column
veggieListBrowserSorted = []
for veggie in veggieList_addr:
    veggieListBrowserSorted.append(veggie.text)
print("Original sorted browser list:", veggieListBrowserSorted)

originalsortedbrowserlist = veggieListBrowserSorted.copy()  # Store the original sorted list for comparison
veggieListBrowserSorted.sort()  # Sort the list using Python's built-in sort method modifyt the original list but dont return anything hence we did not captured it in new list.
print("New sorted list:", veggieListBrowserSorted)

assert originalsortedbrowserlist == veggieListBrowserSorted
print("Sorting is working fine. Both lists are same.")
driver.close()  # Close the child window
driver.switch_to.window(handles[0])  # Switch back to the original window
print("Test Completed Successfully")

driver.quit()