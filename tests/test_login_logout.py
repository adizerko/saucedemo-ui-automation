from pages.login_page import LoginPage
import allure


@allure.feature("Авторизация пользователя")
class TestAuth:

    @allure.story("Логин пользователя")
    @allure.title("Проверка успешного входа с валидными данными")
    def test_login(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу логина"):
            login_page.open()

        with allure.step("Вводим логин и пароль и нажимаем Login"):
            login_page.login()

        with allure.step("Проверяем, что пользователь успешно вошёл"):
            assert login_page.is_logged_in()


    @allure.story("Выход пользователя")
    @allure.title("Проверка успешного выхода из аккаунта")
    def test_logout(self, login):
        inventory_page = login

        with allure.step("Выходим из аккаунта через меню"):
            inventory_page.logout()

        with allure.step("Проверяем, что пользователь вернулся на страницу логина"):
            assert inventory_page.is_logout_in()
