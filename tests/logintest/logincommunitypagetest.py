"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from base.webdriver import WebDriver
from pages.loginpage.logincommunitypage import LoginCommunityPage
from pages.navigationpage.navigationpage import NavigationPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginApplicationPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.initiate_webdriver()
        cls.driver = cls.webdriver_instance.driver
        user = NavigationPage(cls.driver)
        user.navigate_community()

    def test_1_new_applicant_login_valid(self):
        logging.info("##### BEGIN VALID COMMUNITY LOGIN NEW APPLICANT TEST #####")
        user = LoginCommunityPage(self.driver)
        user.login_community(email="evan@fonda.com", first_name="eva", last_name="Fonda", password="WelcomeToSFDC2018!")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        # if cls.driver is not None:
        #     logging.info("# Removing Webdriver #")
        #     cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
