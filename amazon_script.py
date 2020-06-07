from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# init driver
driver: WebDriver = webdriver.Chrome(executable_path='/Users/user/PycharmProjects/JobEasyAuto/AutoClass2/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

# driver.find_element(By.ID, 'twotabsearchtextbox').clear().send_keys("Dress")
input_field = driver.find_element(By.ID, 'twotabsearchtextbox')
input_field.send_keys("Dress")

# driver.find_element(By.XPATH, "//input[@value='Go']").click()
search_icon = driver.find_element(By.XPATH, "//input[@value='Go']")
search_icon.click()

text = driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
assert text == '"Dress"', f'Incorrect text: {text}'
