from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    input_y = browser.find_element(By.ID, "answer")
    input_y.send_keys(y)

    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
