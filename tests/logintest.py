"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from utilities.webdriver import WebDriver
from pages.loginpage import LoginPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.getWebDriverInstance()
        cls.driver = cls.webdriver_instance.driver

    def test_oneLoginValid(self):
        logging.info("##### BEGIN VALID LOGIN TEST #####")
        log_in = LoginPage(self.driver)
        log_in.login_page("test-jcwwd1expiuf@example.com", "m#$M*ZGxv9")
        result = log_in.is_valid()
        self.assertTrue(result)
        print("Valid Login Test Passed")

    def test_twoLoginInvalid(self):
        logging.info("##### BEGIN INVALID LOGIN TEST #####")
        log_in = LoginPage(self.driver)
        log_in.invalid_login_page("test-invalid@example.com", "login")
        result = log_in.is_invalid()
        self.assertEqual(result, "Please check your username and password. "
                         "If you still can't log in, contact your Salesforce administrator.")
        print("Invalid Login Test Passed")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()