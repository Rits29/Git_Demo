from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()  # maximize the browser window
driver.implicitly_wait(2) 

#When no element is found error comes then see if you have frame in the html page.
#If yes then switch to the frame to find element on frame.
#due to website access issue frame focus is not working here.
driver.switch_to.frame("mce_0_ifr")  # switch to the iframe by its name or ID
driver.find_element(By.XPATH, "//div[@aria-label='Close']").click()  # click on the paragraph element inside the iframe
driver.find_element(By.ID,"tinymce").clear()  # clear the text in the paragraph element
driver.find_element(By.ID,"tinymce").send_keys("Hello I am on the Frame right now.")
time.sleep(4)  # wait for 2 seconds to see the text being entered

driver.switch_to.default_content()  # switch back to the default content (main page)
print(driver.find_element(By.XPATH, "//h3").text)

driver.quit()  # close the browser
print("Test completed successfully")
# Note: Always switch back to the default content after performing actions inside an iframe.
# This is important to avoid any issues while interacting with elements outside the iframe.
# If you don't switch back, you won't be able to interact with elements outside the iframe until you switch back to the default content.
# You can also switch to an iframe by its index or by using the `find_element` method to locate the iframe element and then switch to it.