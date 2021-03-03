from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):
    welcome = (By.ID, "mat-dialog-0")
    dismiss = (By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']")
    cookie_message = (By.ID, "cookieconsent:desc")
    we_mean_it = (By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']")

    def __init__(self, driver):
        Page.__init__(self, driver)

    def get_welcome_text(self):
        self.wait_visibility(*self.welcome)
        return self.get_text(*self.welcome)

    def dismiss_welcome(self):
        self.clk_element(*self.dismiss)
        self.wait_invisibility(*self.welcome)

    def get_cookie_message(self):
        return self.get_text(*self.cookie_message)

    def dismiss_cookie_message(self):
        self.clk_element(*self.we_mean_it)
        self.wait_invisibility(*self.cookie_message)
