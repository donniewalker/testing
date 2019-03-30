"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class WebDriver:

    def get_webdriver_instance(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "C:/Users/dowalker/PycharmProjects/chromedriver.exe"
        chrome_driver = "/Users/donniewalker/PycharmProjects/lib/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        self.base_url = "https://test.salesforce.com"
        self.window_before = self.driver.window_handles[0]
        logging.info("##### SETUP TEST #####")
        logging.info("# Initializing Webdriver #")
        # self.driver.maximize_window()
        self.driver.get(self.base_url)
