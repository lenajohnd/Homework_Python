from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")
sleep(2)
driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(2)
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(2)
driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()

success_element = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print("Сообщение:", success_element.text)
sleep(2)

driver.quit()

# sleep написала после каждого шага, чтобы посмотреть, как выполняется скрипт.
