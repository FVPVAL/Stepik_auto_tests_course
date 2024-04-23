from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys("Пупкин")
    browser.find_element(By.NAME, "lastname").send_keys("Иван")
    browser.find_element(By.NAME, "email").send_keys("sdf@rambler.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "2.2.8.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(15)
    browser.quit()
