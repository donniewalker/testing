"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

import logging
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class WebdriverInstance:
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        """
        This method is to instantiate the web driver instance.
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "/Users/donniewalker/PycharmProjects/lib/chromedriver"
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        base_url = "https://test.salesforce.com"
        driver.implicitly_wait(3)
        driver.get(base_url)
        window_before = driver.window_handles[0]
        logging.info(window_before)
        return driver