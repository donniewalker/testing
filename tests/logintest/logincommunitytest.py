"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from base.webdriver import WebDriver
from pages.loginpage.logincommunitypage import LoginCommunityPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginCommunityTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.get_webdriver_instance()
        cls.driver = cls.webdriver_instance.driver

    def test_one_login_new_applicant_valid(self):
        logging.info("##### BEGIN VALID COMMUNITY LOGIN TEST #####")
        log_in = LoginCommunityPage(self.driver)
        log_in.community_apply("jane@fonda.com", "Jane", "Fonda")
        # result = log_in.is_valid()
        # self.assertTrue(result)
        # print("Valid Login Community Test Passed")

    # def test_two_login_invalid(self):
    #     logging.info("##### BEGIN INVALID LOGIN TEST #####")
    #     log_in = LoginPage(self.driver)
    #     log_in.invalid_login_page("test-invalid@login.com", "login")
    #     result = log_in.is_invalid()
    #     self.assertEqual(result, "Please check your username and password. "
    #                      "If you still can't log in, contact your Salesforce administrator.")
    #     print("Invalid Login Test Passed")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
