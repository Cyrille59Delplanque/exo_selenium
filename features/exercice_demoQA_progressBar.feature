Feature: Progress Bar

Scenario: Progress bar is playing to the end
  Given I am connected to the demoQA website
  And I am on the Progress Bar page
  When I start the Progress Bar
  Then Progress Bar is going to the end
