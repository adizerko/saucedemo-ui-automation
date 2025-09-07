"""Страница InventoryPage для проекта SauceDemo.

Содержит методы для взаимодействия с меню пользователя,
выхода из аккаунта и проверки статуса выхода.
"""

import allure
from selenium.webdriver.common.by import By

from curl import LOGIN_PAGE
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Страница инвентаря (Inventory Page) после входа в систему.

    Содержит методы для взаимодействия с меню пользователя и выхода из аккаунта.
    """

    MENU_BUTTON: tuple[str, str] = By.XPATH, '//button[@id="react-burger-menu-btn"]'
    LOGOUT_BUTTON: tuple[str, str] = By.ID, "logout_sidebar_link"
    INVENTORY_CONTAINER: tuple[str, str] = By.ID, "inventory_container"

    @allure.step("Открываем меню пользователя")
    def open_menu(self) -> None:
        self.click_on_element(self.MENU_BUTTON)

    @allure.step('Нажимаем кнопку "Logout"')
    def click_on_button_logout(self) -> None:
        self.click_on_element(self.LOGOUT_BUTTON)

    @allure.step("Выход из аккаунта")
    def logout(self) -> None:
        self.open_menu()
        self.click_on_button_logout()

    @allure.step("Проверяем что мы успешно вышли из аккаунта")
    def is_logout_in(self) -> bool:
        self.wait_for_url_site(LOGIN_PAGE)
        return self.get_current_url() == LOGIN_PAGE
