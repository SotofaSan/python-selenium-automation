from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


RESULTS = (By.XPATH, "//div[@id = 'zg_tabs']/ul/li")


@given('Open Amazon Best Sellers page')
def open_amazon_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(4)

@then('Verify the number of links is {number}')
def verify_5_links_text(context, number):
    search_results = context.driver.find_elements(*RESULTS)
    assert len(search_results) == int(number), "Expected number of links'{}', but got '{}'".format(number, len(search_results))
