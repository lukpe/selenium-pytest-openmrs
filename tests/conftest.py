import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager import ChromeDriverManager, GeckoDriverManager

from config.test_base import TestBase


def pytest_addoption(parser):
    default = TestBase.get_config('driver', 'default')
    parser.addoption('--browser', action='store', default=default)


@pytest.fixture(scope='class')
def setup(request):
    driver = None
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        ChromeDriverManager().download_and_install()
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        GeckoDriverManager().download_and_install()
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(TestBase.get_config('test', 'url'))
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, TestBase.get_config('driver', 'wait'))
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()
