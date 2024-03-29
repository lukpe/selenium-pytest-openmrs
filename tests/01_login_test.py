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

        rand_location = login_page.draw_session_location()
        log.info(
            "Log In: %s",
            f"Username: {user_login} | Password: {user_password} | Location: {rand_location}",
        )
        login_page.log_in(
            user=user_login, password=user_password, location=rand_location
        )
        if is_correct:
            log.info("Expect user to log in")
            assert "Home" in home_page.get_title()
            assert (
                f"Logged in as Super User (admin) at {rand_location}."
                in home_page.get_header()
            )
        elif not is_correct:
            log.info("Expect error message")
            assert "Login" in login_page.get_title()
            assert (
                "Invalid username/password. Please try again."
                in login_page.get_error_messsage()
            )
