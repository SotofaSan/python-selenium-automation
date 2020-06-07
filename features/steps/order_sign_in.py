from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


ORDER_ICON = (By.ID, 'nav-orders')
SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


@when('Click Orders Icon')
def click_search_icon(context):
    context.driver.find_element(*ORDER_ICON).click()
    sleep(1)


@then('Verify Sign in page appeared')
def verify_sign_in_page(context):
    search_result_header = context.driver.find_element(*SIGN_IN_TEXT).text
    assert "Sign-In" in search_result_header #, f'Expected word '{search_word}'