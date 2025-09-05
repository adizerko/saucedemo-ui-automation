from selenium.webdriver.common.by import By
from curl import LOGIN_PAGE, INVENTORY_PAGE
from pages.base_page import BasePage
import allure


class InventoryPage(BasePage):
    MENU_BUTTON = By.XPATH, '//button[@id="react-burger-menu-btn"]'
    LOGOUT_BUTTON = By.ID, 'logout_sidebar_link'
    INVENTORY_CONTAINER = By.ID, 'inventory_container'

    @allure.step('Открытие страницы входа')
    def open(self):
        return self.driver.get(INVENTORY_PAGE)

    @allure.step('Открываем меню пользователя')
    def open_menu(self):
        self.click_on_element(self.MENU_BUTTON)

    @allure.step('Нажимаем кнопку "Logout"')
    def click_on_button_logout(self):
        self.click_on_element(self.LOGOUT_BUTTON)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.open_menu()
        self.click_on_button_logout()

    @allure.step('Проверяем что мы успешно вышли из аккаунта')
    def is_logout_in(self):
        self.wait_for_url_site(LOGIN_PAGE)
        return self.get_current_url() == LOGIN_PAGE
