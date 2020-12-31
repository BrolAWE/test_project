import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("C:/Users/aleks/Downloads/chromedriver_win32/chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
