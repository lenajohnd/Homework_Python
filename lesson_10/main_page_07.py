from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class MainPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы магазина.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по названию.

        Args:
            product_name: Название товара для добавления в корзину

        Raises:
            ValueError: Если товар с указанным названием не найден
        """
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

    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self) -> None:
        """Переходит в корзину покупок, нажимая на значок корзины."""
        self.driver.find_element(*self.cart_badge).click()
