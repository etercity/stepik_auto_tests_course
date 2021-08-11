import pytest
from selenium import webdriver
from configs import sittings
import time
import math

all_messages = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=sittings.DRIVER)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(all_messages)

@pytest.mark.parametrize('links', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    global all_messages
    browser.implicitly_wait(10)
    browser.get(links)
    answer = str(math.log(int(time.time())))
    textarea = browser.find_element_by_css_selector("textarea.ember-text-area")
    textarea.send_keys(answer)
    # Отправляем число
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    check = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == check
    except AssertionError:
        all_messages += check  # собираем ответы с ошибками


