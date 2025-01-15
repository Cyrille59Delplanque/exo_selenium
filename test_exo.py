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

@pytest.fixture
def browser():
    #Assurer vous que le pilote est installé et configuré correctement
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
@scenario('features/e', 'Select all elements except Office and Excel file.doc')
    
