from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def calculate(self, num1, operator, num2):
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button("=")

    def wait_for_result(self, expected_result, timeout=46):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            lambda driver: driver.find_element(*self.screen).text == expected_result
        )

    def get_result(self):
        return self.driver.find_element(*self.screen).text
