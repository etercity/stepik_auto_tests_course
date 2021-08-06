from selenium import webdriver
from configs import sittings
import time


try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    # browser.execute_script("document.title='Script executing';")
    # browser.execute_script("alert('Robots at work');")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()









