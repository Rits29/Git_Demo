from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Implicit wait: This is used to set a default waiting time for all elements in the script. It will wait 
# for the specified time before throwing an exception if an element is not found. In case the element is found 
# before the desired time, it will proceed immediately, by saving us the remaining wait time. In slenium its advised to
# use implicit wait only once in the script, at the start of the script and not the time.sleep() function because 
# this will save us from waiting unnecessarily for the elements that are already loaded 
# and by calling time function again and again.
# Explicit wait: This is used to wait for a specific condition to occur before proceeding with the next step.
# It is more flexible than implicit wait as it allows you to wait for a specific element or condition.
# Explicit wait is used when we want to wait for a specific element to be present, visible, clickable, etc.
# It is more efficient than implicit wait as it waits only for the specified condition to be met.

driver.maximize_window() 
print("Website opened successfully")

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("Ca")
#driver.find_element(By.XPATH, "//button[@class='search-button']").click()
print("Search completed successfully")
time.sleep(5)
# Explicit wait can be used here if we want to wait for the products to be loaded 
#wait = WebDriverWait(driver, 10)  # seconds
#wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='products']/div")))
#all_products = driver.find_elements(By.XPATH, "//div[@class='products']/div")  #By.XPATH, "//div[@class='products']/div"
#products = [p for p in all_products if p.is_displayed()]
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
n = len(products)
print("Number of products found:", n)
assert n > 0

#for i in range(n):
 #   products = driver.find_elements(By.CSS_SELECTOR, "div.products div.product")
    # Get fresh product
  #  product = products[i]
    # Get fresh button inside that product
   # button = product.find_element(By.XPATH, ".//button")
    #button.click()
    #print(f"Clicked on Add button for product #{i+1}")

for product in products:
    #button = WebDriverWait(product, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "div/button")))
    #button.click()
    # Alternatively, we can use the following line to click the button.  By.XPATH, ".//button"
    product.find_element(By.XPATH,"div/button").click() # don't add // in front of div/button here as we are chaining the elements
    print("Clicked on Add button for product.")


driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[class="promoCode"]').send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
#time.sleep(4)
act_text = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
assert "Code applied ..!" in act_text
print("Promo code applied successfully")

#validate the total price
costs = driver.find_elements(By.XPATH, "//tbody/tr/td[5]")
sum = 0
for cost in costs:
    sum +=int(cost.text)
print("Total cost of products in cart:", sum)
act_cost = driver.find_element(By.XPATH, "//span[@class='totAmt']").text
assert int(act_cost) == sum
print("Total cost is validated successfully")
#place the order
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
#time.sleep(2)
select = Select(driver.find_element(By.XPATH, "//div/select"))
select.select_by_visible_text("India")
driver.find_element(By.XPATH, '//input[@class="chkAgree"]').click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
print("Order placed successfully")


driver.quit()
print("Browser closed successfully")