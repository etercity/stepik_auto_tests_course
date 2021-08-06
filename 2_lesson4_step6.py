from selenium import webdriver
from configs import sittings
import time


try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get("http://suninjuly.github.io/cats.html")

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)

    browser.find_element_by_id("button")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()





