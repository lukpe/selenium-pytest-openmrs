from selenium.webdriver.common.by import By

from pages.base_page import Page


class LoginPage(Page):
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    loginButton = (By.ID, 'loginButton')

    def __init__(self, driver):
        Page.__init__(self, driver)

    def log_in(self, **kwargs):
        self.set_element_text(*self.username, value=kwargs['user'])
        self.set_element_text(*self.password, value=kwargs['password'])
        location_element = (By.ID, kwargs['location'])
        self.clk_element(*location_element)
        self.clk_element(*self.loginButton)
