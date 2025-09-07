"""Фикстуры и настройки pytest для проекта SauceDemo.

Содержит:
- настройку браузера (Chrome/Firefox) с использованием Selenoid,
- фикстуру `driver` для работы с WebDriver,
- фикстуру `login` для авторизации перед тестами.
"""

from collections.abc import Generator
from typing import TYPE_CHECKING, Any

import pytest
from _pytest.config import Parser  # type: ignore[attr-defined]
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

import curl
from curl import SELENOID_URL
from data import BROWSERS
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

if TYPE_CHECKING:
    from selenium.webdriver.common.options import BaseOptions  # только для type hints

def pytest_addoption(parser: Parser) -> None:
    """Добавляем опцию --browser и --browser-version для выбора браузера при запуске pytest."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox",
    )
    parser.addoption(
        "--browser-version",
        action="store",
        default=None,
        help="Browser version to run tests",
    )


@pytest.fixture
def driver(request: FixtureRequest) -> Generator[WebDriver, Any, None]:
    """Создаёт и возвращает WebDriver в зависимости от выбранного браузера."""
    browser = request.config.getoption("--browser").lower()
    version = request.config.getoption("--browser-version")

    if browser not in BROWSERS:
        msg = f"Browser {browser} is not supported. Supported: {list(BROWSERS.keys())}"
        raise ValueError(msg)

    if not version:
        version = BROWSERS[browser][0]

    if version not in BROWSERS[browser]:
        msg = f"Version {version} for {browser} is not available. Supported: {BROWSERS[browser]}"
        raise ValueError(msg)

    options: BaseOptions
    if browser == "chrome":
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", version)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("browserName", "firefox")
        options.set_capability("browserVersion", version)
    else:
        msg = f"Браузер {browser} не поддерживается"
        raise ValueError(msg)

    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False,
    })

    driver = webdriver.Remote(
        command_executor=SELENOID_URL,
        options=options,
    )

    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def login(driver: WebDriver) -> InventoryPage:
    """Авторизует пользователя и возвращает InventoryPage."""
    login_page = LoginPage(driver, curl.LOGIN_PAGE)
    login_page.open()
    login_page.login()
    return InventoryPage(driver, curl.LOGIN_PAGE)
