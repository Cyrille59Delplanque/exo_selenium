Feature: Menu

Scenario: Menu is showing when hover
  Given I am connected to the demoQA website
  And I am on the Menu page
  When I navigate through Main Item2
  And I navigate through SUB SUB LIST
  Then I select sub sub Item2
