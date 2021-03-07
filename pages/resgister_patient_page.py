import calendar

from selenium.webdriver.common.by import By

from pages.base_page import Page
from utils.test_data import PatientData


class RegisterPatientPage(Page):
    next_button = (By.ID, 'next-button')
    given_name = (By.NAME, 'givenName')
    family_name = (By.NAME, 'familyName')
    gender_field = (By.ID, 'gender-field')
    birth_day = (By.ID, 'birthdateDay-field')
    birth_month = (By.ID, 'birthdateMonth-field')
    birth_year = (By.ID, 'birthdateYear-field')
    address1 = (By.ID, 'address1')
    city = (By.ID, 'cityVillage')
    country = (By.ID, 'country')
    postal_code = (By.ID, 'postalCode')
    phone_numer = (By.NAME, 'phoneNumber')
    add_relationship = (By.CSS_SELECTOR, 'a[ng-click=\'addNewRelationship()\']')

    def __init__(self, driver):
        Page.__init__(self, driver)

    def fill_patient_data(self):
        data = PatientData.get_data()
        self.set_element_text(*self.given_name, value=data['first_name'])
        self.set_element_text(*self.family_name, value=data['last_name'])
        self.clk_element(*self.next_button)

        self.select_option_by_text(*self.gender_field, option='Female')
        self.clk_element(*self.next_button)
        birth_date = data['birth_date']
        self.set_element_text(*self.birth_day, value=birth_date.day)
        self.select_option_by_text(*self.birth_month, option=calendar.month_name[birth_date.month])
        self.set_element_text(*self.birth_year, value=birth_date.year)
        self.clk_element(*self.next_button)

        self.set_element_text(*self.address1, value=data['addr_street'])
        self.set_element_text(*self.city, value=data['addr_city'])
        self.set_element_text(*self.country, value=data['addr_country'])
        self.set_element_text(*self.postal_code, value=data['addr_postal'])
        self.clk_element(*self.next_button)

        self.set_element_text(*self.phone_numer, value=data['addr_phone'])
        self.clk_element(*self.next_button)

        relatives = []
        for i in range(2):
            relationship_type = (By.XPATH, f'//div[@class=\'ng-scope\']//div[{i + 1}]//p[1]//select[1]')
            self.select_option_random(*relationship_type)
            selection = self.get_selected(*relationship_type)
            person_name = (By.XPATH, f'//div[@class=\'ng-scope\']//div[{i + 1}]//p[2]//input[1]')
            random_name = PatientData.get_value(value='name')
            self.set_element_text(*person_name, value=random_name)
            relatives.append((selection, random_name))
            self.clk_element(*self.add_relationship)
        self.clk_element(*self.next_button)
