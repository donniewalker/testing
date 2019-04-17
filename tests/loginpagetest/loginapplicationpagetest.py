
import logging
import unittest

from base.webdriver import WebDriver
from pages.loginpage.loginapplicationpage import LoginApplicationPage
from pages.navigationpage.navigationpage import NavigationPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginApplicationPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver = WebDriver()
        cls.webdriver.initiate_webdriver()
        cls.driver = cls.webdriver.driver
        user = NavigationPage(cls.driver)
        user.navigate_application()

    def test_1_new_applicant_login_valid(self):
        logging.info("##### BEGIN VALID COMMUNITY LOGIN NEW APPLICANT TEST #####")
        user = LoginApplicationPage(self.driver)
        user.login_application(email="eva@fondaa.com", first_name="eva", last_name="Fonda",
                               password="WelcomeToSFDC2018!")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
