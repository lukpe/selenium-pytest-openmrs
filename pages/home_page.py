from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):
    header = (By.TAG_NAME, 'H4')
    register = (By.ID,
                'referenceapplication-registrationapp-registerPatient-homepageLink-referenceapplication'
                '-registrationapp-registerPatient-homepageLink-extension')

    def __init__(self, driver):
        Page.__init__(self, driver)

    def get_header(self):
        return self.get_text(*self.header)

    def register_patient(self):
        self.clk_element(*self.register)
