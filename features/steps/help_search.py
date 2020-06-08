from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'helpsearch')
SEARCH_SUBMIT = (By.CSS_SELECTOR, 'input.a-button-input')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='help-content']/h1")


@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
    sleep(1)


@when('Input {search_word} into Find More Solutions field')
def input_find_more_solutions(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(1)

@when('Click on Go icon')
def click_go_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

@then('Text {search_word} is shown')
def verify_cancel_order_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)

