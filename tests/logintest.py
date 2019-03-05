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

    def setUp(self):
        self.webdriver_instance = WebDriver()
        self.webdriver_instance.getWebDriverInstance()
        self.driver = self.webdriver_instance.driver

    def test_oneValidLogin(self):
        logging.info("## BEGIN VALID LOGIN TEST ##")
        login_page = LoginPage(self.driver)
        login_page.login("test-jcwwd1expiuf@example.com", "m#$M*ZGxv9")
        result = login_page.loginSuccessful()
        assert result == True
        print("Valid Login Test Passed")

    def tearDown(self):
        logging.info("## TEARDOWN TEST ##")
        if self.driver is not None:
            logging.info("# Removing Webdriver #")
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()