from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_patient_page import RegisterPatientPage
from utils.test_base import TestBase


class TestInpatientWard(TestBase):
    def test_register_patient(self):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        register_page = RegisterPatientPage(self.driver)

        log.info("Log in")
        login_page.log_in(user="Admin", password="Admin123", location="Inpatient Ward")
        log.info("Fill in patient data")
        home_page.register_patient()
        register_page.fill_patient_name()
        register_page.fill_patient_gender()
        register_page.fill_patient_birthdate()
        register_page.fill_patient_address()
        register_page.fill_patient_phone_number()
        register_page.fill_patient_relatives("random")
        log.info("Verify patient data")
        register_page.verify_patient_data()
        log.info("Confirm submission")
        register_page.confirm_submission()
