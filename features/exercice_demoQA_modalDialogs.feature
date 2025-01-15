Feature: Modal Dialogs

Scenario: Verify occurences in a text
  Given I am connected to the demoQA website
  And I am on the Modal Dialogs page
  When Read the text in the large modal window
  Then "lorem ipsum" is found 4 occurences
