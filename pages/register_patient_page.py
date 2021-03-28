import calendar
import random

from selenium.webdriver.common.by import By

from pages.base_page import Page
from utils.test_data import PatientData


class RegisterPatientPage(Page):
    next_button = (By.ID, "next-button")
    given_name = (By.NAME, "givenName")
    family_name = (By.NAME, "familyName")
    gender_field = (By.ID, "gender-field")
    birth_day = (By.ID, "birthdateDay-field")
    birth_month = (By.ID, "birthdateMonth-field")
    birth_year = (By.ID, "birthdateYear-field")
    address1 = (By.ID, "address1")
    city = (By.ID, "cityVillage")
    country = (By.ID, "country")
    postal_code = (By.ID, "postalCode")
    phone_number = (By.NAME, "phoneNumber")
    add_relationship = (By.CSS_SELECTOR, "a[ng-click='addNewRelationship()']")
    data_canvas = (By.XPATH, "//div[@id='dataCanvas']/div/p")
    confirm_button = (By.ID, "submit")

    def __init__(self, driver):
        Page.__init__(self, driver)
        vars(self).update(PatientData.get_data())
        self.relatives = []

    def fill_patient_name(self):
        self.set_element_text(*self.given_name, value=self.first_name)
        self.set_element_text(*self.family_name, value=self.last_name)
        self.clk_element(*self.next_button)

    def fill_patient_gender(self):
        self.select_option_by_text(*self.gender_field, option=self.gender)
        self.clk_element(*self.next_button)

    def fill_patient_birthdate(self):
        birth_date = self.split_birth_date()
        self.set_element_text(*self.birth_day, value=birth_date[0])
        self.select_option_by_text(*self.birth_month, option=birth_date[1])
        self.set_element_text(*self.birth_year, value=birth_date[2])
        self.clk_element(*self.next_button)

    def split_birth_date(self):
        birth_date = self.birth_date
        day = birth_date.day
        month = calendar.month_name[birth_date.month]
        year = birth_date.year
        return (day, month, year)

    def fill_patient_address(self):
        self.set_element_text(*self.address1, value=self.addr_street)
        self.set_element_text(*self.city, value=self.addr_city)
        self.set_element_text(*self.country, value=self.addr_country)
        self.set_element_text(*self.postal_code, value=self.addr_postal)
        self.clk_element(*self.next_button)

    def fill_patient_phone_number(self):
        self.set_element_text(*self.phone_number, value=self.addr_phone)
        self.clk_element(*self.next_button)

    def fill_patient_relatives(self, number):
        if number == "random":
            number = random.randint(2, 5)
        for i in range(number):
            relationship_type = (
                By.XPATH,
                f"//div[@class='ng-scope']//div[{i + 1}]//p[1]//select[1]",
            )
            self.wait_visibility(*relationship_type)
            relation = self.select_option_random(*relationship_type)
            selection = self.get_selected(*relationship_type)
            person_name = (
                By.XPATH,
                f"//div[@class='ng-scope']//div[{i + 1}]//p[2]//input[1]",
            )
            random_name = PatientData.get_relative_name(i + 1, relation)
            self.wait_visibility(*person_name)
            self.set_element_text(*person_name, value=random_name)
            self.relatives.append((selection, random_name))
            if i < (number - 1):
                self.clk_element(*self.add_relationship)
        self.clk_element(*self.next_button)

    def verify_patient_data(self):
        elements = self.get_elements(*self.data_canvas)
        assert elements[0].text == f"Name: {self.first_name}, {self.last_name}"
        assert elements[1].text == f"Gender: {self.gender}"
        birth_date = self.split_birth_date()
        assert (
            elements[2].text
            == f"Birthdate: {birth_date[0]}, {birth_date[1]}, {birth_date[2]}"
        )
        assert (
            elements[3].text == f"Address: {self.addr_street}, {self.addr_city}, "
            f"{self.addr_country}, {self.addr_postal}"
        )
        assert elements[4].text == f"Phone Number: {self.addr_phone}"
        assert "Relatives: " in elements[5].text
        for relative in self.relatives:
            assert f"{relative[1]} - {relative[0]}" in elements[5].text

    def confirm_submission(self):
        self.clk_element(*self.confirm_button)
        self.wait_invisibility(*self.confirm_button)
