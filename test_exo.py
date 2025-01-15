import pytest
import pytest_bdd
from pytest_bdd import parsers
from pytest_bdd import scenario,given,when,then
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def browser():
    #Select Chrome as Browser for test
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
@scenario('features/exercice_demoQA_checkBox.feature', 'Select all elements except Office and Excel file.doc')
def test_checkBox():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous
@scenario('features/exercice_demoQA_webTables.feature', 'Modify Web tables')  
def test_webTables():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous
# @scenario('features/exercice_demoQA_browserWindows.feature',"Opening/Closing a Tab")
# @scenario('features/exercice_demoQA_modalDialogs.feature',"Verify occurences in a text")
# @scenario('features/exercice_demoQA_progressBar.feature',"Progress bar is playing to the end")
# @scenario('features/exercice_demoQA_menu.feature',"Menu is showing when hover")
# @scenario('features/exercice_demoQA_selectMenu.feature',"Select Menu play")
@scenario('features/exercice_demoQA_bookStore.feature',"Search a book by Author")
def test_bookStore():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous


connection_str = 'I am connected to the demoQA website'
@given(connection_str)
def open_demoQA_website(browser):
    # Open Website
    browser.get("https://demoqa.com")
    print(connection_str)
    
@given('I am on the CheckBox page')
def go_to_checkbox_page(browser):   
    # Click on the Element link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(1)").click()
    # Click on the CheckBox link
    browser.find_element(By.XPATH, "//li[@id=\'item-1\']").click()
    
@given('I am on the Web Tables page')
def go_to_checkbox_page(browser):   
    # Click on the Element link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(1)").click()
    # Click on the CheckBox link
    browser.find_element(By.XPATH, "//li[@id=\'item-3\']").click()
    
@given('I am on the Browser Windows page')
def go_to_browser_windows_page(browser):
    # Click on Alert, Frame & Windows link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(3)").click()
    # Click on Browser Windows link
    browser.find_element(By.CSS_SELECTOR, ".show #item-0 > .text").click()
    
@given('I am on the Modal Dialogs page')
def go_to_modal_dialogs_page(browser):
    # Click on Alert, Frame & Windows link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(3)").click()
    # Click on Model Dialog link
    browser.find_element(By.CSS_SELECTOR, ".show #item-4 > .text").click()
    
@given('I am on the Progress Bar page')
def go_to_progress_bar_page(browser):
    # Click on Widgets link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(4)").click()
    # Click on Progress Bar link
    browser.find_element(By.CSS_SELECTOR, ".show #item-4 > .text").click()
    
@given('I am on the Menu page')
def go_to_menu_page(browser):
    #set to max screen size
    browser.set_window_size(2560, 1440)
    # Click on Widgets link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(4)").click()
    # Click on Menu link
    browser.find_element(By.CSS_SELECTOR, ".show #item-7 > .text").click()
    
@given('I am on the Select Menu page')
def go_to_select_menu_page(browser):
    # Click on Widgets link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(4)").click()
    # Click on Select Menu link
    browser.find_element(By.CSS_SELECTOR, ".show #item-8 > .text").click()
    
@given('I am on the Book Store page')
def go_to_book_store_page(browser):
    # Click on Book Store Application link
    browser.find_element(By.CSS_SELECTOR, ".card:nth-child(6)").click()

@when('I select all elements except Office and Excel file.doc')
def select_elements(browser):
    # Click on the Expand all button
    browser.find_element(By.XPATH, "//*[@title=\"Expand all\"]").click()
    # Click on the Home element to select all checkBoxes
    browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Home\']").click()
    # Click on the Office element to unselect it
    browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Office\']").click()
    # Click on the Excel File.doc element to unselect it
    browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Excel File.doc\']").click()
    
@when('I delete the last two lines')
def delete_first_two_lines(browser):
    browser.find_element(By.XPATH, "//*[@id=\"delete-record-3\"]").click()
    browser.find_element(By.XPATH, "//*[@id=\"delete-record-2\"]").click()
    
@when('set the salary to 4300')
def set_salary_to_first_line(browser):
    browser.find_element(By.XPATH, "//*[@id=\"edit-record-1\"]").click()
    browser.find_element(By.XPATH, "//*[@id=\"salary\"]").clear()
    browser.find_element(By.XPATH, "//*[@id=\"salary\"]").send_keys("4300")
    browser.find_element(By.XPATH, "//*[@id=\"submit\"]").click()
    

@when('I add a new tab', target_fixture='original_window')
def add_new_tab(browser):
    original_window = browser.current_window_handle
    browser.find_element(By.ID, "tabButton").click()
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break
    return original_window

@when('close the added tab')
def close_added_tab(browser):
    browser.close()
    

@when('Read the text in the large modal window')
def search_text_in_modal(browser):
    #go the large modal window
    browser.find_element(By.ID, "showLargeModal").click()
    
# I start the Progress Bar
@when('I start the Progress Bar')
def start_progress_bar(browser):
    browser.find_element(By.ID, "startStopButton").click()
    
@when('I navigate through Main Item2')
def navigate_through_main_item2(browser):
    # Hover on Main Item 2
    time.sleep(0.3) #for stability
    ActionChains(browser).move_to_element(browser.find_element(By.LINK_TEXT, "Main Item 2")).perform()
    
@when('I navigate through SUB SUB LIST')
def navigate_through_sub_sub_list(browser):
    # Hover on Sub Sub List
    ActionChains(browser).move_to_element(browser.find_element(By.LINK_TEXT, "SUB SUB LIST »")).perform()
    
@when('I choose to enter "Another root option"  "other" "aqua" "red" "black"')
def enter_data_in_select_menu(browser):
    # Click on Select Value to Display a menu
    browser.find_element(By.ID, "withOptGroup").click()
    #Select Another root option
    browser.find_element(By.ID, "react-select-2-option-3").click()
    #Click in Select One
    browser.find_element(By.ID, 'selectOne').click()
    #Select Other
    browser.find_element(By.ID, "react-select-3-option-0-5").click()
    dropdown = browser.find_element(By.ID, "oldSelectMenu")
    dropdown.find_element(By.XPATH, "//option[. = 'Aqua']").click()
    #Select Multiselect dropdown
    css_selector = '#selectMenuContainer > div:nth-child(8) > div > div > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder'
    browser.find_element(By.CSS_SELECTOR,css_selector ).click()
    browser.find_element(By.ID, "react-select-4-option-3").click()
    browser.find_element(By.ID, "react-select-4-option-2").click()
    browser.find_element(By.CSS_SELECTOR,css_selector ).click()
    
@when('I search the author "Marijn Haverbeke"')
def search_author(browser):
    browser.find_element(By.ID, "searchBox").send_keys("Marijn Haverbeke")
    browser.find_element(By.ID, "searchBox").send_keys(Keys.ENTER)
  
@then('all elements are checked except Office and Excel file.doc')
def control_elements(browser):
    #mauvais à changer
    assert not browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Office\']").is_selected()
    
@then('there is only one line')
def check_number_of_lines(browser):
    number_of_line = len(browser.find_elements(By.XPATH, "//div[@class=\'rt-tr-group\']"))
    line_not_empty = 0
    for i in range(1, number_of_line + 1):
        css_selector_indexed = ".rt-tr-group:nth-child(" + str(i) + ") .rt-td:nth-child(1)"
        if browser.find_element(By.CSS_SELECTOR,css_selector_indexed).text != " ":
            line_not_empty += 1
    assert line_not_empty == 1
    
@then('the salary is 4300')
def control_salary(browser):
    assert browser.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(1) .rt-td:nth-child(5)").text == "4300"
    
@then('I am in the initial tab')
def original_tab(browser,original_window):
    assert len(browser.window_handles) == 1
    browser.switch_to.window(original_window)
    
@then('"lorem ipsum" is found 4 occurences')
def find_occurences(browser):
    time.sleep(0.2)
    #take the text
    text = browser.find_element(By.XPATH, "//p").text
    #search the text "lorem ipsum"
    assert text.count("Lorem Ipsum") == 4
    
@then('Progress Bar is going to the end')
def control_progress_bar(browser):
    WebDriverWait(browser, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar > div"), "100%"))

@then('I select sub sub Item2')
def click_on_sub_sub_item2(browser):
    browser.find_element(By.LINK_TEXT, "SUB SUB LIST »").click()
    
@then('nothing happens')
def nothing_happens(browser):
    pass

@then('The books of the author "Marijn Haverbeke" are displayed')
def check_books_of_author(browser):
    assert browser.find_element(By.CSS_SELECTOR, ".rt-tbody > div:nth-of-type(1) div:nth-of-type(2)").text == "Eloquent JavaScript, Second Edition","test"
  
