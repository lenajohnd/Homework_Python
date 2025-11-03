from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.username_field = (By.CSS_SELECTOR, "#user-name")
        self.password_field = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """Открывает страницу авторизации в браузере."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Выполнить авторизацию пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя.

        Args:
            username: Имя пользователя
            password: Пароль пользователя
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
