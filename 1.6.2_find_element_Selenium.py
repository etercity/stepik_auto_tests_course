from selenium import webdriver
from selenium.webdriver.common.by import By

from configs import sittings

try:
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    # button = browser.find_element_by_id("submit_button")
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

