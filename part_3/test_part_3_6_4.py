from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


def test_authorization(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys("izol@rambler.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("Qwet5j")
    browser.find_element(By.CSS_SELECTOR, ".button_with-loader").click()
    time.sleep(5)
