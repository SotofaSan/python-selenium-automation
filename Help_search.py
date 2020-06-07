# Test Case:
# User can search for solutions of Cancelling an order on Amazon
# 1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
# 2. Use “Find more solutions” field and search for Cancel order:
# 3. Click Go
# 4. Verify that ‘Cancel Items or Orders’ text is present

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# init driver
driver: WebDriver = webdriver.Chrome(executable_path='/Users/user/PycharmProjects/JobEasyAuto/AutoClass2/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# 1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.implicitly_wait(4)

# 2. Use “Find more solutions” field and search for Cancel order:
input_field = driver.find_element(By.ID, 'helpsearch')
input_field.clear()
input_field.send_keys("Cancel order")

# 3. Click Go
search_icon = driver.find_element(By.XPATH, "//span[@class='a-button-inner']/input[@type='submit']")
search_icon.click()

# 4. Verify that ‘Cancel Items or Orders’ text is present
text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
assert text == 'Cancel Items or Orders', f'Incorrect text: {text}'