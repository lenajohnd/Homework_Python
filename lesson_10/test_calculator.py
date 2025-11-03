from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page import CalculatorPage
import allure
import pytest


@allure.title("Тест медленного калькулятора")
@allure.description("Проверка работы калькулятора с установленной задержкой вычислений")
@allure.feature("Calculator Operations")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    """Тестирует работу калькулятора с задержкой вычислений."""

    driver: WebDriver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    try:
        with allure.step("Настройка калькулятора"):
            calculator.open()
            calculator.set_delay(45)

        with allure.step("Выполнение вычисления 7 + 8"):
            calculator.calculate("7", "+", "8")

        with allure.step("Ожидание и проверка результата"):
            result = calculator.wait_for_result("15")
            assert calculator.get_result() == "15", "Результат вычислений неверный"

        with allure.step("Проверка корректности результата"):
            assert calculator.get_result() == "15", f"Ожидалось 15, получено {calculator.get_result()}"

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()