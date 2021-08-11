import pytest
from selenium import webdriver

chrome_driver = './drivers/chromedriver.exe'
firefox_driver = './drivers/geckodriver.exe'


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=chrome_driver)
    # browser = webdriver.Firefox(executable_path=firefox_driver) #для фокса
    yield browser
    print("\nquit browser..")
    browser.quit()


