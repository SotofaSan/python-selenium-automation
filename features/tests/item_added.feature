# Created by user at 6/7/2020
Feature: Test Scenarios for Cart functionality
  # Create your own test case to add any product you want into the cart,
  # make sure it’s there
  # (check for the number of items in the cart OR open the cart and verify it’s there, up to you!)

  Scenario: Item is added to the cart
    Given Open Amazon Pen search page
    When Click on pen item image
    And Click on Add to Cart icon
    Then Verify Added to Cart alert