from selenium import webdriver
from configs import sittings
import time


try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get("http://suninjuly.github.io/wait1.html")

    # time.sleep(5)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




