# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Dress into search field
    And Click on search icon
    Then Product results for Dress are shown