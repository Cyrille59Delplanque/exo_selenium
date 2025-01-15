Feature: Book Store

Scenario: Search a book by Author
  Given I am connected to the demoQA website
  And I am on the Book Store page
  When I search the author "Marijn Haverbeke"
  Then The books of the author "Marijn Haverbeke" are displayed
