import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils.test_base import TestBase


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TestBase.get_config("driver", "wait"))
        self.actions = ActionChains(self.driver)

    def get_title(self):
        return self.driver.title

    def get_text(self, *loc):
        return self.driver.find_element(*loc).text

    def get_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def clk_element(self, *loc):
        self.driver.find_element(*loc).click()

    def move_and_clk_element(self, *loc):
        element = self.driver.find_element(*loc)
        self.actions.move_to_element(element).click(element).perform()

    def select_option_by_text(self, *loc, option):
        select = Select(self.driver.find_element(*loc))
        select.select_by_visible_text(option)

    def select_option_random(self, *loc):
        select = Select(self.driver.find_element(*loc))
        options = select.options
        option = random.choice(options)
        select.select_by_visible_text(option.text)
        return option.text

    def select_element_random(self, *loc):
        elements = self.get_elements(*loc)
        element = random.choice(elements)
        element.click()
        return element.text

    def get_selected(self, *loc):
        select = Select(self.driver.find_element(*loc))
        option = select.first_selected_option
        return option.text

    def set_element_text(self, *loc, value):
        self.driver.find_element(*loc).send_keys(value)

    def wait_visibility(self, *loc):
        self.wait.until(ec.visibility_of_element_located((*loc,)))

    def wait_invisibility(self, *loc):
        self.wait.until(ec.invisibility_of_element_located((*loc,)))
