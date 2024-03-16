from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    span = browser.find_element(By.ID, "input_value")
    x = span.text
    y = calc(x)
    input_y = browser.find_element(By.ID, "answer")
    input_y.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()

finally:
    time.sleep(15)
    browser.quit()
