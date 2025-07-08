from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()  # maximize the browser window

#click on the link to open a new window
driver.find_element(By.CSS_SELECTOR,'a').click()
handles = driver.window_handles  # get all the window handles which are opened in list format are stored in handles
print("Number of windows opened:", len(handles))
driver.switch_to.window(handles[1])  
# switch to the child window. Parent window is at index 0 and child window is at index 1
time.sleep(4)  # wait for 2 seconds to let the child window load
copy_text = driver.find_element(By.XPATH, '//div[@class="col-md-8"]/p[2]').text
print(copy_text)  # print the text from the child window
driver.close()  # close the child window
driver.switch_to.window(handles[0])  # switch back to the parent window
#enter the username and password in the parent window by extracting the text from the child window
driver.find_element(By.ID, "username").send_keys(copy_text.split(" ")[4])  # extract username from the text
driver.find_element(By.ID, "password").send_keys(copy_text.split(" ")[6])  # extract password from the text
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,'//input[@type="checkbox"]')).click().perform() 
# click on the checkbox
action.move_to_element(driver.find_element(By.ID, "signInBtn")).click().perform()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


#error_msg = driver.find_element(By.XPATH, "//form[@id='login-form']/div[1]").text # click on the OK button
#print(error_msg)  # print the text from the alert
#assert "Incorrect" in error_msg # Verify the text in the alert
driver.quit()  # Close the browser
print("Test completed successfully")
# Note: This code demonstrates how to handle a child window in Selenium,
# extract text from it, and use that text to perform actions in the parent window.
# It also shows how to handle alerts in Selenium.
# Make sure to always switch back to the parent window after performing actions on the child window,
# and close the child window to free up resources.
# This is a common scenario in web automation where you need to interact with multiple windows or popups.
# Always remember to handle alerts properly to avoid any interruptions in your test flow.
# This code is a good example of how to handle child windows and alerts in Selenium.
# It can be extended further to handle more complex scenarios involving multiple child windows or popups.
# Always ensure to close the browser at the end of the test to free up resources.
# This code can be used as a reference for handling child windows and alerts in Selenium tests.