from config.test_base import TestBase
from pages.home_page import HomePage


class TestSample(TestBase):

    def test_page_title(self):
        log = self.get_logger()
        hp = HomePage(self.driver)

        log.info('Verifying page title')
        assert 'DuckDuckGo' in hp.get_title()
