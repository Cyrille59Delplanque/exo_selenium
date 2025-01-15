Feature: Web Tables

Scenario: Modify Web tables
  Given I am connected to the demoQA website
  And I am on the Web Tables page
  When I delete the last 2 lines 
  And set the salary to 4300
  Then there is only 1 line
  And the salary is 4300
