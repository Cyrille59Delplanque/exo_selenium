Feature: CheckBox

 Scenario: Select all elements except Office and Excel File.doc
   Given I am connected to the demoQA website
   And I am on the Check Box page
   When I select all elements except Office and Excel File.doc
   Then all elements are checked except Office and Excel File.doc