from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.CSS_SELECTOR, "#first-name")
        self.last_name_field = (By.CSS_SELECTOR, "#last-name")
        self.postal_code_field = (By.CSS_SELECTOR, "#postal-code")
        self.continue_button = (By.CSS_SELECTOR, "#continue")
        self.total_label = (By.CSS_SELECTOR, '[data-test="total-label"]')

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self):
        return self.driver.find_element(*self.total_label).text