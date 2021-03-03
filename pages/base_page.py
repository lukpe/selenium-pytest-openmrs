from selenium.webdriver.support.wait import WebDriverWait

from config.test_base import TestBase


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TestBase.get_config('driver', 'wait'))

    def get_title(self):
        return self.driver.title
