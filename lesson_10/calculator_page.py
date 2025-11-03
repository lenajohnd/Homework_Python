from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.delay_field = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку вычислений: {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку вычислений в калькуляторе.

        Args:
            seconds: Количество секунд задержки
        """
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажать кнопку: {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку калькулятора по тексту.

        Args:
            button_text: Текст на кнопке (цифра или оператор)
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    @allure.step("Выполнить вычисление: {num1} {operator} {num2}")
    def calculate(self, num1: str, operator: str, num2: str) -> None:
        """
        Выполняет математическую операцию.

        Args:
            num1: Первое число
            operator: Оператор (+, -, *, /)
            num2: Второе число
        """
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button("=")

    @allure.step("Ожидать результат: {expected_result}")
    def wait_for_result(self, expected_result: str, timeout: int = 46) -> bool:
        """
        Ожидает появления ожидаемого результата на экране.

        Args:
            expected_result: Ожидаемый результат вычислений
            timeout: Максимальное время ожидания в секундах

        Returns:
            bool: True если результат появился, иначе False
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            lambda driver: driver.find_element(*self.screen).text == expected_result
        )

    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """
        Получает текущий результат с экрана калькулятора.

        Returns:
            str: Текст результата вычислений
        """
        return self.driver.find_element(*self.screen).text
