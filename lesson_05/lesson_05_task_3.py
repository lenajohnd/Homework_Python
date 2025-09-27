from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.XPATH, "//input[@type='number']")
sleep(2)
input_field.click()
sleep(2)
input_field.send_keys("Sky")
sleep(2)
input_field.clear()
sleep(2)
input_field.send_keys("Pro")
sleep(2)

driver.quit()

# sleep написала после каждого шага, чтобы посмотреть, как выполняется скрипт.
