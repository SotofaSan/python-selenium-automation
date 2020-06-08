from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


SEARCH_SUBMIT = (By.ID, 'nav-cart')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class = 'a-row sc-your-amazon-cart-is-empty']/h2")


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Verify {search_word} is shown')
def verify_cart_is_empty_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)
