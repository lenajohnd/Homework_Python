from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def add_to_cart(self, product_name):
        product_id_map = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }

        product_id = product_id_map.get(product_name)
        if product_id:
            add_button = (By.CSS_SELECTOR, f"#{product_id}")
            self.driver.find_element(*add_button).click()
        else:
            raise ValueError(f"Товар '{product_name}' не найден")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_badge).click()
