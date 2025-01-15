Feature: CheckBox
  As a user
  I want to check the checkbox
  So that I can select the option

 Scenario: Select all elements except Office and Excel file.doc
   Given I am connected to the demoQA website
   When I check all elements except Office and Excel file.doc
   Then all elements are checked except Office and Excel file.doc
   