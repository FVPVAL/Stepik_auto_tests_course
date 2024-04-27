import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("link", ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_3_6_5(browser, link):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys("izol@rambler.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("Qwet5j")
    browser.find_element(By.CSS_SELECTOR, ".button_with-loader").click()
    if len(browser.find_elements(By.CSS_SELECTOR, ".again-btn")) > 0:
        browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
    answer = math.log(int(time.time()))
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(answer)
    but = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    but.click()
    x = WebDriverWait(browser, 10).until(EC.visibility_of_element_located
                                         ((By.CSS_SELECTOR, ".smart-hints__hint"))).text

    assert "Correct!" == x
