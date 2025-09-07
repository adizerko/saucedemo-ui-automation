"""Страница LoginPage для проекта SauceDemo.

Содержит методы для ввода имени пользователя и пароля,
клика по кнопке Login и проверки успешного входа.
"""

import allure
from selenium.webdriver.common.by import By

from curl import INVENTORY_PAGE
from data import PASSWORD, USERNAME
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница логина (Login Page).

    Содержит методы для открытия страницы логина, ввода учетных данных,
    нажатия кнопки входа и проверки успешного входа.
    """

    USERNAME_INPUT: tuple[str, str] = By.XPATH, '//input[@id="user-name"]'
    PASSWORD_INPUT: tuple[str, str] = By.XPATH, '//input[@id="password"]'
    LOGIN_BUTTON: tuple[str, str] = By.XPATH, '//input[@id="login-button"]'

    @allure.step("Ввод имени пользователя")
    def set_username(self) -> None:
        self.send_keys_to_input(self.USERNAME_INPUT, USERNAME)

    @allure.step("Ввод пароля пользователя")
    def set_password(self) -> None:
        self.send_keys_to_input(self.PASSWORD_INPUT, PASSWORD)

    @allure.step('Кликаем на кнопку "Login"')
    def click_on_button_login(self) -> None:
        self.click_on_element(self.LOGIN_BUTTON)

    @allure.step("Вход в систему")
    def login(self) -> None:
        self.set_username()
        self.set_password()
        self.click_on_button_login()

    def is_logged_in(self) -> bool:
        self.wait_for_url_site(INVENTORY_PAGE)
        return self.get_current_url() == INVENTORY_PAGE
