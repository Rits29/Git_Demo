#Scroll Functionality
# Javascript Events 
#We execute the javascript code using the execute_script method of the driver object.
#Head and Headless Browsing. In Headless mode, the browser runs without a GUI, which is useful for 
#   automated testing and scraping tasks where you don't need to see the browser window.
# Selenium can ignore all the certificate errors using the `accept_untrusted_certs` option, 
#   SSL errors, and other security warnings.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller  

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  # Run in headless mode
#chrome_options.add_argument("--ignore-certificate-errors")  # Disable the ceritificate errors

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/large")
time.sleep(2)  # Wait for the page to load

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # Scroll to the bottom of the page
time.sleep(2)  # Wait for 2 seconds to see the scroll effect
driver.get_screenshot_as_file("screenshot.png")  # Take a screenshot of the page
