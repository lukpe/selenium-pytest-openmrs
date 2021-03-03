from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config.test_base import TestBase


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TestBase.get_config('driver', 'wait'))

    def get_title(self):
        return self.driver.title

    def get_text(self, *loc):
        return self.driver.find_element(*loc).text

    def clk_element(self, *loc):
        self.driver.find_element(*loc).click()

    def wait_visibility(self, *loc):
        self.wait.until(ec.visibility_of_element_located((*loc,)))

    def wait_invisibility(self, *loc):
        self.wait.until(ec.invisibility_of_element_located((*loc,)))
