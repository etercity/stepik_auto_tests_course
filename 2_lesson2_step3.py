from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from configs import sittings


link1 = "http://suninjuly.github.io/selects1.html"
link2 = " http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get(link2)

    num1 = browser.find_element_by_id("num1")
    num1 = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    num2 = int(num2.text)
    summa = num1+num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





