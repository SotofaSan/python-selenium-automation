
# Created by user at 6/7/2020
Feature:  Test Scenarios for Cart functionality
  #3. Create a test case using BDD that opens amazon.com,
# clicks on the cart icon and
# verifies that Your Shopping Cart is empty.

  Scenario: The cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Verify Your Amazon Cart is empty is shown