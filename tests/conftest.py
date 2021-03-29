import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager import ChromeDriverManager, GeckoDriverManager
from utils.excel_driver import ExcelDriver
from utils.test_base import TestBase


def pytest_addoption(parser):
    default = TestBase.get_config("driver", "default")
    parser.addoption("--browser", action="store", default=default)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.option.htmlpath:
        date = time.strftime("%y%m%d")
        path = os.path.dirname(os.path.abspath(__file__))
        config.option.htmlpath = f"{path}\\..\\output\\report_{date}.html"


@pytest.fixture(scope="function")
def setup(request):
    # Setup driver
    driver = None
    browser = request.config.getoption("browser")
    if browser == "chrome":
        ChromeDriverManager().download_and_install()
        driver = webdriver.Chrome()
    elif browser == "firefox":
        GeckoDriverManager().download_and_install()
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(TestBase.get_url())
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, TestBase.get_config("driver", "wait"))
    request.cls.driver = driver
    request.cls.wait = wait
    # Setup TestData.xlsx
    ExcelDriver().set_workbook()
    yield
    driver.quit()
