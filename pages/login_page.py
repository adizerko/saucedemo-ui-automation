from selenium.webdriver.common.by import By
from curl import LOGIN_PAGE, INVENTORY_PAGE
from pages.base_page import BasePage
from data import *
import allure


class LoginPage(BasePage):
    USERNAME_INPUT = By.XPATH, '//input[@id="user-name"]'
    PASSWORD_INPUT = By.XPATH, '//input[@id="password"]'
    LOGIN_BUTTON = By.XPATH, '//input[@id="login-button"]'

    @allure.step('Открытие страницы входа')
    def open(self):
        return self.driver.get(LOGIN_PAGE)

    @allure.step('Ввод имени пользователя')
    def set_username(self):
        self.send_keys_to_input(self.USERNAME_INPUT, username)

    @allure.step('Ввод пароля пользователя')
    def set_password(self):
        self.send_keys_to_input(self.PASSWORD_INPUT, password)

    @allure.step('Кликаем на кнопку "Login"')
    def click_on_button_login(self):
        self.click_on_element(self.LOGIN_BUTTON)

    @allure.step('Вход в систему')
    def login(self):
        self.set_username()
        self.set_password()
        self.click_on_button_login()

    def is_logged_in(self):
        self.wait_for_url_site(INVENTORY_PAGE)
        return self.get_current_url() == INVENTORY_PAGE
