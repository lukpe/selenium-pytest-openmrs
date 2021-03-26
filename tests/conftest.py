import urllib.request, urllib.error
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager import ChromeDriverManager, GeckoDriverManager
from utils.excel_driver import ExcelDriver
from utils.test_base import TestBase


def pytest_addoption(parser):
    default = TestBase.get_config("driver", "default")
    parser.addoption("--browser", action="store", default=default)


def get_url():
    url_local = TestBase.get_config("test", "url_local")
    url = TestBase.get_config("test", "url")
    try:
        status_code = urllib.request.urlopen(url_local).getcode()
        if status_code == 200:
            return url_local
    except urllib.error.HTTPError:
        pass
    except urllib.error.URLError:
        pass
    return url


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
    driver.get(get_url())
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, TestBase.get_config("driver", "wait"))
    request.cls.driver = driver
    request.cls.wait = wait
    # Setup TestData.xlsx
    ExcelDriver().set_workbook()
    yield
    driver.quit()
