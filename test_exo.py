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
    
dico_main_page = {"Elements":1,
                  "Forms":2,
                  "Alerts, Frame & Windows":3,
                  "Widgets":4,
                  "Interactions":5,
                  "Book Store Application":6}

dico_page = {"Text Box":0,
                      "Check Box":1,
                      "Radio Button":2,
                        "Web Tables":3,
                        "Buttons":4,
                        "Links":5,
                        "Broken Links - Images":6,
                        "Upload and Download":7,
                        "Dynamic Properties":8,
                        "Browser Windows":0,
                    "Alerts":1,
                    "Frames":2,
                    "Nested Frames":3,
                    "Modal Dialogs":4,
                    "Accordian":0,
                     "Auto Complete":1,
                     "Date Picker":2,
                     "Slider":3,
                     "Progress Bar":4,
                     "Tabs":5,
                     "Tool Tips":6,
                     "Menu":7,
                     "Select Menu":8,
                     "Sortable":0,
                          "Selectable":1,
                          "Resizable":2,
                          "Droppable":3,
                          "Dragabble":4,
                          "Login":0,
                        "Book Store":1,
                        "Profile":2,
                        "Book Store API":3}

dico_page_connection = {"Check Box":["Elements","Check Box"],
                        "Web Tables":["Elements","Web Tables"],
                        "Browser Windows":["Alerts, Frame & Windows","Browser Windows"],
                        "Modal Dialogs":["Alerts, Frame & Windows","Modal Dialogs"],
                        "Progress Bar":["Widgets","Progress Bar"],
                        "Menu":["Widgets","Menu"],
                        "Select Menu":["Widgets","Select Menu"],
                        "Book Store":["Book Store Application","Book Store"]}
    
@scenario('features/exercice_demoQA_checkBox.feature', 'Select all elements except Office and Excel File.doc')
def test_checkBox():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_webTables.feature', 'Modify Web tables')  
def test_webTables():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_browserWindows.feature',"Opening/Closing a Tab")
def test_browserWindows():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_modalDialogs.feature',"Verify occurences in a text")
def test_modalDialogs():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_progressBar.feature',"Progress bar is playing to the end")
def test_progressBar():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_menu.feature',"Menu is showing when hover")
def test_menu():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_selectMenu.feature',"Select Menu play")
def test_selectMenu():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous

@scenario('features/exercice_demoQA_bookStore.feature',"Search a book by Author")
def test_bookStore():
    pass #les étapes réelles du test seront executées par les implémentations d'étapes ci-dessous


connection_site_str = 'I am connected to the demoQA website'
@given(connection_site_str)
def open_demoQA_website(browser):
    # Open Website
    browser.get("https://demoqa.com")
    print(connection_site_str)
    
connection_page_str = 'I am on the {feature_name} page' 
@given(parsers.parse(connection_page_str))    
# @given(parsers.parse('I am on the {feature_name} page'))
def go_to_page(browser,feature_name):
    name_to_log = connection_page_str.replace("{feature_name}",feature_name)
    # Click on the main menu link
    list_connect = dico_page_connection[feature_name]
    index_to_select = dico_main_page[list_connect[0]]
    css_selector = ".card:nth-child(" + str(index_to_select) + ")"
    browser.find_element(By.CSS_SELECTOR, css_selector).click()
    # Click on the Detail Menu link
    if feature_name not in ["Book Store"]:
        index_to_select = dico_page[list_connect[1]]
        css_selector = ".show #item-" + str(index_to_select) + " > .text"
        browser.find_element(By.CSS_SELECTOR, css_selector).click()
        #Control Test of Page selected to be sure of the right page
        xpath_control = "//h1[@class='text-center']"
        text_of_page = browser.find_element(By.XPATH,xpath_control).text
        assert text_of_page == feature_name
        print(name_to_log)
    else:
        print(name_to_log)

action = 'I select all elements except {element_1} and {element_2}'
@when(parsers.parse(action))
def select_elements(browser,element_1,element_2):
    action_to_log = action.replace("{element_1}",element_1)
    action_to_log = action_to_log.replace("{element_2}",element_2)
    # Click on the Expand all button
    browser.find_element(By.XPATH, "//*[@title=\"Expand all\"]").click()
    # Click on the Home element to select all checkBoxes
    xpath_to_click = "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Home\']"
    browser.find_element(By.XPATH, xpath_to_click).click()
    # Click on the element_1 to unselect it
    xpath_to_click = "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'"+element_1+"\']"
    browser.find_element(By.XPATH, xpath_to_click).click()
    #browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Office\']").click()
    # Click on the element2 to unselect it
    xpath_to_click = "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'"+element_2+"\']"
    browser.find_element(By.XPATH, xpath_to_click).click()
    # browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Excel File.doc\']").click()
    print(action_to_log)

@when('I delete the last 2 lines')
def delete_last_two_lines(browser):
    browser.find_element(By.XPATH, "//*[@id=\"delete-record-3\"]").click()
    browser.find_element(By.XPATH, "//*[@id=\"delete-record-2\"]").click()
    print('I delete the last 2 lines')
    
@when('set the salary to 4300')
def set_salary_to_first_line(browser):
    browser.find_element(By.XPATH, "//*[@id=\"edit-record-1\"]").click()
    browser.find_element(By.XPATH, "//*[@id=\"salary\"]").clear()
    browser.find_element(By.XPATH, "//*[@id=\"salary\"]").send_keys("4300")
    browser.find_element(By.XPATH, "//*[@id=\"submit\"]").click()
    print('set the salary to 4300')

@when('I add a new tab', target_fixture='original_window')
def add_new_tab(browser):
    original_window = browser.current_window_handle
    browser.find_element(By.ID, "tabButton").click()
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break
    print('I add a new tab')
    return original_window

@when('close the added tab')
def close_added_tab(browser):
    browser.close()
    print('close the added tab')
    

@when('Read the text in the large modal window')
def search_text_in_modal(browser):
    #go the large modal window
    browser.find_element(By.ID, "showLargeModal").click()
    print('Read the text in the large modal window')
    
# I start the Progress Bar
@when('I start the Progress Bar')
def start_progress_bar(browser):
    browser.find_element(By.ID, "startStopButton").click()
    print('I start the Progress Bar')
    
@when('I navigate through Main Item2')
def navigate_through_main_item2(browser):
    # Hover on Main Item 2
    time.sleep(1) #for stability
    ActionChains(browser).move_to_element(browser.find_element(By.LINK_TEXT, "Main Item 2")).perform()
    print('I navigate through Main Item2')
    
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
    time.sleep(1.5)
    browser.find_element(By.ID, "searchBox").send_keys("Marijn Haverbeke")
    browser.find_element(By.ID, "searchBox").send_keys(Keys.ENTER)
  
@then('all elements are checked except Office and Excel File.doc')
def control_elements(browser):
    #mauvais à changer
    assert not browser.find_element(By.XPATH, "//div[@id=\'tree-node\']//span[@class=\'rct-text\']//span[.=\'Office\']").is_selected()
  
action ='there is only {number_of_line_to_have} line' 
# @then('there is only 1 line')
@then(parsers.parse(action))
def check_number_of_lines(browser,number_of_line_to_have):
    action_to_log = action.replace("{number_of_line_to_have}",number_of_line_to_have)
    number_of_line = len(browser.find_elements(By.XPATH, "//div[@class=\'rt-tr-group\']"))
    line_not_empty = 0
    for i in range(1, number_of_line + 1):
        css_selector_indexed = ".rt-tr-group:nth-child(" + str(i) + ") .rt-td:nth-child(1)"
        if browser.find_element(By.CSS_SELECTOR,css_selector_indexed).text != " ":
            line_not_empty += 1
    assert line_not_empty == int(number_of_line_to_have) #1
    print(action_to_log)
    
   
@then('the salary is 4300')
def control_salary(browser):
    assert browser.find_element(By.CSS_SELECTOR, ".rt-tr-group:nth-child(1) .rt-td:nth-child(5)").text == "4300"
    print("The salary is 4300")
    
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
  
