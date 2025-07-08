from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.maximize_window()  # maximize the browser window
driver.implicitly_wait(10)  # seconds

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver) #create object of ActionChains and pass driver instance

action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform() #move to the element
action.context_click(driver.find_element(By.XPATH, "//a[@href='#top']")).perform() #context click on the element

driver.close()
