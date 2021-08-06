from selenium import webdriver
import time
from configs import sittings


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get(link2)

    first_name = browser.find_element_by_css_selector(".first_block :nth-child(1) input")
    first_name.send_keys("Alex")
    first_name = browser.find_element_by_css_selector(".first_block :nth-child(2) input")
    first_name.send_keys("QA")
    first_name = browser.find_element_by_css_selector(".first_block :nth-child(3) input")
    first_name.send_keys("etercity@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

