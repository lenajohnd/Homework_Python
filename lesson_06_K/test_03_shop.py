from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shopping_cart_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_badge").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Helen")
    driver.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Aleshina")
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("662546")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    element = driver.find_element(
        By.CSS_SELECTOR, '[data-test="total-label"]')
    assert element.text == "Total: $58.29"

    driver.quit()
