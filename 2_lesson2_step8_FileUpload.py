from selenium import webdriver
import time
import os
from configs import sittings


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input[name='firstname']")
    first_name.send_keys("Alex")
    first_name = browser.find_element_by_css_selector("input[name='lastname']")
    first_name.send_keys("QA")
    first_name = browser.find_element_by_css_selector("input[name='email']")
    first_name.send_keys("etercity@gmail.com")
    select_file = browser.find_element_by_id("file")
    select_file.send_keys(file_path)


    # Отправляем заполненную форму & file
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



