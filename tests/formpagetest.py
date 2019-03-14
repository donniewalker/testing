"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest
import time

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
        # log_in = LoginPage(cls.driver)
        # log_in.login_page("test-ctbawsg8setw@example.com", "y$9lB0|YDD")

    def test_submit_guestcard(self):
        logging.info("##### BEGIN SUBMIT FULL FORM #####")
        self.driver.get("https://sandbox-efficiency-page-8761-1694a6059cf.cs69.force.com/s/"
                        "guest-card?moc=On_Site&propertyId=a1B2D0000003JtUUAU&pNum=679")
        time.sleep(3)
        submit_full_form = FormPage(self.driver)
        submit_full_form.submit_form_all("Henry", "Hen", "Madison", "1234 Yorktown St", "New Hampshire", "67567",
                                         "3546789876", "henry@madison.com")
        # result = log_in.is_valid()
        # self.assertTrue(result)
        # print("Valid Login Test Passed")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()