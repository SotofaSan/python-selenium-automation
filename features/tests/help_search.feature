# Created by user at 6/7/2020
# Test Case:
# User can search for solutions of Cancelling an order on Amazon
# 1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
# 2. Use “Find more solutions” field and search for Cancel order:
# 3. Click Go
# 4. Verify that ‘Cancel Items or Orders’ text is present
Feature: Testing Amazon Help page

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon Help page
    When Input Cancel order into Find More Solutions field
    And Click on Go icon
    Then Text Cancel Items or Orders is shown
