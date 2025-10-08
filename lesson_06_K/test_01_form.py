from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    driver = webdriver.Edge()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    driver.find_element(
        By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    current_url = driver.current_url

    driver.find_element(
        By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: d.current_url != current_url)

    assert "data-types-submitted" in driver.current_url

    zip_code_element = driver.find_element(
        By.CSS_SELECTOR, '#zip-code')
    assert "alert-danger" in zip_code_element.get_attribute("class")

    green_elements = [
        '#first-name', '#last-name', '#address', '#e-mail', '#phone',
        '#city', '#country', '#job-position', '#company'
    ]

    for element_id in green_elements:
        element = driver.find_element(By.CSS_SELECTOR, element_id)
        assert "alert-success" in element.get_attribute("class")

    driver.quit()
