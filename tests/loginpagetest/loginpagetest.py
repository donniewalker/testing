
import logging
import unittest

from base.webdriver import WebDriver
from pages.loginpage.loginpage import LoginPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.get_webdriver_instance()
        cls.driver = cls.webdriver_instance.driver

    def test_1_valid_login(self):
        logging.info("##### BEGIN VALID LOGIN TEST #####")
        user = LoginPage(self.driver)
        result = user.valid_login("test-txc52mkpywff@example.com", "p@ta0CB2)M")
        self.assertTrue(result)

    def test_2_invalid_login(self):
        logging.info("##### BEGIN INVALID LOGIN TEST #####")
        user = LoginPage(self.driver)
        result = user.invalid_login("test-invalid@login.com", "login")
        self.assertEqual(result, "Please check your username and password. "
                                 "If you still can't log in, contact your Salesforce administrator.")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
