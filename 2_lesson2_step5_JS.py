from selenium import webdriver
from configs import sittings
import time


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get(link)
    # button = browser.find_element_by_tag_name("button")
    # button.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()





