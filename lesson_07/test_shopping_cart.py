from selenium import webdriver
from login_page_07 import LoginPage
from main_page_07 import MainPage
from cart_page_07 import CartPage
from checkout_page_07 import CheckoutPage


def test_shopping_cart_total():
    driver = webdriver.Firefox()

    # Инициализация Page Objects
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        main_page.add_to_cart("Sauce Labs Backpack")
        main_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        main_page.add_to_cart("Sauce Labs Onesie")

        main_page.go_to_cart()

        cart_page.checkout()

        checkout_page.fill_checkout_form("Helen", "Aleshina", "662546")

        total_text = checkout_page.get_total_amount()
        assert total_text == "Total: $58.29"

    finally:
        driver.quit()
