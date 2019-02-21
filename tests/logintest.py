"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

import unittest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.loginpage import LoginPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginTest(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        logging.info("## SETUP METHODs ##")
        logging.info("# Initializing WebDriverInstance.")
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
        lp = LoginPage(self.driver)
        lp.login()
    #     # result = self.lp.verifyLogin Successful()
    #     # assert result == True

    def tearDown(self):
        logging.info("### TEARDOWN METHOD ###")
        logging.info("# Quitting #")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()