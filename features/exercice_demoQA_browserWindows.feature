Feature: Browser Windows

Scenario: Opening/Closing a Tab
  Given I am connected to the demoQA website
  And I am on the Browser Windows page
  When I add a new tab
  And close the added tab
  Then I am in the initial tab
