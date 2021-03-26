import pytest
from utils.test_base import TestBase
from pages.login_page import LoginPage
from pages.home_page import HomePage

test_data = [
    ("Admin", "Admin123", True),
    ("Admin", "", False),
    ("", "Admin123", False),
    ("", "", False),
    ("Test", "Test", False),
]


class TestLoggingIn(TestBase):
    @pytest.mark.parametrize("user_login, user_password, is_correct", test_data)
    def test_login(self, user_login, user_password, is_correct):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        log.info("Log In to the Inpatient Ward")
        login_page.log_in(
            user=user_login, password=user_password, location="Inpatient Ward"
        )
        if is_correct:
            assert "Home" in home_page.get_title()
            assert (
                "Logged in as Super User (admin) at Inpatient Ward."
                in home_page.get_header()
            )
        elif not is_correct:
            assert "Login" in login_page.get_title()
            assert (
                "Invalid username/password. Please try again."
                in login_page.get_error_messsage()
            )
