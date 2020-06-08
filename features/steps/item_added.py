from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ITEM_SUBMIT = (By.XPATH, "//img[@srcset = 'https://m.media-amazon.com/images/I/71hL9YoydnL._AC_SX180_SY120_QL70_.jpg 1x,https://m.media-amazon.com/images/I/71hL9YoydnL._AC_SX360_SY240_QL70_.jpg 2x']")
ADD_SUBMIT = (By.ID, 'add-to-cart-button')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@id = 'huc-v2-order-row-confirm-text']/h1")


@given('Open Amazon Pen search page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/s?k=pen&ref=nb_sb_noss')
    sleep(4)


@when('Click on pen item image')
def click_item_description(context):
    context.driver.find_element(*ITEM_SUBMIT).click()
    sleep(1)


@when('Click on Add to Cart icon')
def click_add_to_cart_icon(context):
    context.driver.find_element(*ADD_SUBMIT).click()
    sleep(1)

@then('Verify {search_word} alert')
def verify_added_to_cart_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)