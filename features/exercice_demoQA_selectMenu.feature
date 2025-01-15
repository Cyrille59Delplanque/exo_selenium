Feature: Select Menu

Scenario: Select Menu play
  Given I am connected to the demoQA website
  And I am on the Select Menu page
  When I choose to enter "Another root option"  "other" "aqua" "red" "black"
  Then nothing happens
