# Created by user at 6/20/2020
Feature:  Test Scenarios for Best Sellers
  #  Create a test case that will open amazon BestSellers page:
  #  https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
  #  And verify there are 5 links:

  Scenario:  Verify 5 links in Best Sellers
    Given Open Amazon Best Sellers page
    Then Verify the number of links is 5