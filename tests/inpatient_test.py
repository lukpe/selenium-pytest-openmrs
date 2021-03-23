from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_patient_page import RegisterPatientPage
from utils.test_base import TestBase


class TestInpatientWard(TestBase):
    def test_login(self):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        log.info('Log In to the Inpatient Ward')
        login_page.log_in(user='Admin', password='Admin123', location='Inpatient Ward')
        assert 'Home' in home_page.get_title()
        assert (
            'Logged in as Super User (admin) at Inpatient Ward.'
            in home_page.get_header()
        )

    def test_register_patient(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        register_page = RegisterPatientPage(self.driver)

        log.info('Register a patient')
        home_page.register_patient()
        register_page.fill_patient_name()
        register_page.fill_patient_gender('Female')
        register_page.fill_patient_birthdate()
        register_page.fill_patient_address()
        register_page.fill_patient_phone_number()
        register_page.fill_patient_relatives(3)
