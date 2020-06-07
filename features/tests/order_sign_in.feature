# 4*. Create a Test Case using BDD (Behave features and steps):
#Test Case:
#Logged out user sees Sign in page when clicking Orders
#
#1. Open https://www.amazon.com
#2. Click Orders
#3. Verify Sign in page opened
Feature: Tests for Help functionality

  Scenario: Verify search for Cancel Order
    Given Open Amazon page
    When Click Orders Icon
    Then Verify Sign in page appeared