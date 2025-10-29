from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    try:
        calculator.open()
        calculator.set_delay(45)
        calculator.calculate("7", "+", "8")
        result = calculator.wait_for_result("15")
        assert calculator.get_result() == "15"

    finally:
        driver.quit()
