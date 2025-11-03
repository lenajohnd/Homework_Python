from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.first_name_field = (By.CSS_SELECTOR, "#first-name")
        self.last_name_field = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_field = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.total_label = (By.CSS_SELECTOR, '[data-test="total-label"]')

    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму личной информации для оформления заказа.

        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Текст с общей суммой заказа
        """
        return self.driver.find_element(*self.total_label).text
