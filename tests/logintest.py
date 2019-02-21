"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

import unittest
import logging

from utilities.webdriver import WebDriverInstance
from pages.loginpage import LoginPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginTest(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_oneValidLogin(self):
        wdi = WebDriverInstance(self.driver)
        wdi.getWebDriverInstance()
        self.lp = LoginPage(self.driver)
        self.lp.login()
        # result = self.lp.verifyLogin Successful()
        # assert result == True

    def tearDown(self):
        logging.info("### TEARDOWN METHOD ###")
        logging.info("# Quitting #")
        self.lp.driver.quit()


if __name__ == "__main__":
    unittest.main()