"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

import logging
import unittest
import sys

from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginTests(unittest.TestCase):
    """
        Instantiate the webdriver instance.
        """

    def setUp(self):
        """
        This method is to instantiate the webdriver instance.
        """
        logging.info("## SETUP METHOD ##")
        logging.info("# Initializing WebDriverInstance. #")
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "/Users/donniewalker/PycharmProjects/lib/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        base_url = "https://test.salesforce.com"
        # self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(base_url)
        window_before = self.driver.window_handles[0]
        logging.info(window_before)

    def test_oneValidLogin(self):
        login_page = LoginPage(self.driver)
        login_page.login("test-ug6swfcwdsa5@example.com", "28)Gg#kH|G")
        # result = self.lp.verifyLogin Successful()
        # assert result == True

    def tearDown(self):
        """
        Teardown method.
        Capture screenshots of failed test cases
        & to quit web driver instance.
        """
        logging.info("### TEARDOWN METHOD ###")

        if sys.exc_info()[0]:
            logging.info("# Say Cheese! #")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# I quit! #")
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()