from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
