"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from base.webdriver import WebDriver
from pages.loginpage import LoginPage
from pages.formpage import FormPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.getWebDriverInstance()
        cls.driver = cls.webdriver_instance.driver
        log_in = LoginPage(cls.driver)
        log_in.login_page("test-ctbawsg8setw@example.com", "y$9lB0|YDD")

    def test_submit_form(self):
        logging.info("##### BEGIN SUBMIT FULL FORM #####")
        submit_full_form = FormPage(self.driver)
        submit_full_form.submit_form_all("Henry", "Hen", "Madison", "1234 Yorktown St", "New Hampshire", "67567",
                                         "3546789876", "henry@madison.com")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
