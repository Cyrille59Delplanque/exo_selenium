Feature: CheckBox

 Scenario: Select all elements except Office and Excel file.doc
   Given I am connected to the demoQA website
   And I am on the CheckBox page
   When I select all elements except Office and Excel file.doc
   Then all elements are checked except Office and Excel file.doc