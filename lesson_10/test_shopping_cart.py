from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from login_page_07 import LoginPage
from main_page_07 import MainPage
from cart_page_07 import CartPage
from checkout_page_07 import CheckoutPage
import allure
import pytest


@allure.title("Тест итоговой суммы корзины покупок")
@allure.description("Проверка корректного расчета общей суммы при добавлении нескольких товаров")
@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.BLOCKER)
def test_shopping_cart_total():
    """Тестирует расчет общей суммы заказа при добавлении нескольких товаров."""

    driver: WebDriver = webdriver.Firefox()

    # Инициализация Page Objects
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Авторизация пользователя"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            main_page.add_to_cart("Sauce Labs Backpack")
            main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
            main_page.add_to_cart("Sauce Labs Onesie")

        with allure.step("Переход в корзину"):
            main_page.go_to_cart()

        with allure.step("Начало оформления заказа"):
            cart_page.checkout()

        with allure.step("Заполнение информации для доставки"):
            checkout_page.fill_checkout_form("Helen", "Aleshina", "662546")

        with allure.step("Проверка итоговой суммы"):
            total_text = checkout_page.get_total_amount()
            expected_total = "Total: $58.29"
            assert total_text == expected_total, f"Ожидалось {expected_total}, получено {total_text}"

    finally:
        with allure.step("Завершение теста и закрытие браузера"):
            driver.quit()
