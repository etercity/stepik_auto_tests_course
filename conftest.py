import pytest
from selenium import webdriver

CHROME_DRIVER = './drivers/chromedriver.exe'
FIREFOX_DRIVER = './drivers/geckodriver.exe'


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(executable_path=chrome_driver)
#     # browser = webdriver.Firefox(executable_path=firefox_driver) #для фокса
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER)  # для фокса
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
