"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class WebdriverInstance():
    """
    Instantiate the webdriver instance.
    """

    def getWebDriverInstance(self):
        """
        This method is to instantiate the webdriver instance.
        """
        logging.info("## SETUP METHOD ##")
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