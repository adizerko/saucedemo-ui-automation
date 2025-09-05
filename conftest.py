from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()
    return InventoryPage(driver)
