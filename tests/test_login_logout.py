"""Тесты авторизации: вход и выход пользователя."""

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

import curl
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Авторизация и выход пользователя") # type: ignore
class TestAuth:
    """Тесты авторизации: вход и выход пользователя."""

    @allure.story("Логин пользователя") # type: ignore
    @allure.title("Проверка аутентификации и авторизации пользователя") # type: ignore
    @allure.description("Проверка возможности входа зарегистрированного пользователя") # type: ignore
    def test_login(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver, curl.LOGIN_PAGE)

        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Вводим логин и пароль и нажимаем Login"):
            login_page.login()

        with allure.step("Проверяем, что пользователь успешно вошёл"):
            assert login_page.is_logged_in()

    @allure.story("Выход пользователя") # type: ignore
    @allure.title("Проверка успешного выхода из аккаунта") # type: ignore
    @allure.description("Проверка возможности выхода авторизованного пользователя из системы")# type: ignore
    def test_logout(self, login: InventoryPage) -> None:
        with allure.step("Логинимся с помощью фикстуры"):
            inventory_page = login

        with allure.step("Выходим из аккаунта через меню"):
            inventory_page.logout()

        with allure.step("Проверяем, что пользователь вернулся на страницу логина"):
            assert inventory_page.is_logout_in()
