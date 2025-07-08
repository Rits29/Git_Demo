from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()  # maximize the browser window
driver.implicitly_wait(10)  # seconds
# Any new window or tab or page which opens up after clicking on a link is called a child window.
# The main window is called the parent window.
# To navigate from Parent to Child window, we need to switch the control from parent to child.
# And vice-versa to switch from child to parent.
print(driver.title)
driver.find_element(By.LINK_TEXT, "Click Here").click()  # click on the link to open a new window
handles = driver.window_handles  # get all the window handles which are opened in list format are stored in handles
print("Number of windows opened:", len(handles))
driver.switch_to.window(handles[1])  # switch to the child window
time.sleep(5)  # wait for 2 seconds to let the child window load
print(driver.title)  # print the title of the child window
driver.close()  # close the child window
driver.switch_to.window(handles[0])  # switch back to the parent window
print(driver.title)  # print the title of the parent window
driver.quit()  # close the browser
print("Test completed successfully")
# Note: Always switch back to the parent window after performing actions on the child window.
# If you don't switch back, you won't be able to perform any actions on the parent window
# until you close the child window.
# Also, if you have multiple child windows, you can switch to any child window using its index in the handles list.
# For example, to switch to the second child window, you can use `driver.switch_to.window(handles[2])`.
# Make sure to always switch back to the parent window after performing actions on the child window,
# otherwise you won't be able to interact with the parent window until you close the child window.
# You can also use `driver.switch_to.default_content()` to switch back to the default content of the page,
# which is useful when you are working with iframes or frames.
# In this case, we are not using any iframes or frames, so we don't need to use `driver.switch_to.default_content()`.
# But it's a good practice to know about it in case you need it in future.
# Always remember to close the child window after performing actions on it,
# otherwise it will remain open and consume resources.
# You can also use `driver.quit()` to close all the windows and end the session,
# but in this case we are using `driver.close()` to close only the child window and then switching back to the parent window.
# This way we can continue to interact with the parent window
# after closing the child window.
# Always make sure to close the browser at the end of the test to free up resources.