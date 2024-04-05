import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistered(unittest.TestCase):

    def test_link1(self):

        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)

        input_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input_name.send_keys("Name")
        input_last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input_last_name.send_keys("Last name")
        input_email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input_email.send_keys("E-mail")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "КОСЯК")

        browser.quit()

    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)

        input_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input_name.send_keys("Name")
        input_last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input_last_name.send_keys("Last name")
        input_email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input_email.send_keys("E-mail")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "КОСЯК")

        browser.quit()


if __name__ == "__main__":
    unittest.main()
