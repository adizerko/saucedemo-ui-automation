"""Базовый класс для всех страниц проекта.

Содержит общие методы для взаимодействия с веб-элементами:
- ожидание элементов,
— клики,
— ввод текста,
— получение URL и т.д.
"""

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Базовый класс для всех страниц."""

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Инициализация страницы с переданным WebDriver."""
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу сайта")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельности элемента")
    def wait_for_clickable(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator: tuple[str, str], timeout: int = 10) -> None:
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator: tuple[str, str], keys: str, timeout: int =10) -> None:
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)


    @allure.step("Ожидаем загрузки страницы URL")
    def wait_for_url_site(self, url: str, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url),
        )

    @allure.step("Получаем текущий адрес сайта")
    def get_current_url(self) -> str:
        """Возвращает текущий URL страницы."""
        return self.driver.current_url
