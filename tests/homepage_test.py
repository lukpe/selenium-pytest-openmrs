from config.test_base import TestBase
from pages.home_page import HomePage


class TestHomePage(TestBase):

    def test_page_elements(self):
        log = self.get_logger()
        home_p = HomePage(self.driver)

        log.info('Verifying page title')
        assert 'OWASP Juice Shop' in home_p.get_title()
        assert 'Welcome to OWASP Juice Shop!' in home_p.get_welcome_text()
        home_p.dismiss_welcome()
        cookie_text = 'This website uses fruit cookies to ensure you get ' \
                      'the juiciest tracking experience'
        assert cookie_text in home_p.get_cookie_message()
        home_p.dismiss_cookie_message()
