
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class WebDriver:

    def __init__(self):
        chrome_driver = "/Users/donniewalker/PycharmProjects/lib/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver)
        self.base_url = "https://test.salesforce.com"

    def get_webdriver_instance(self):
        logging.info("##### SETUP TEST #####")
        logging.info("# Initializing Webdriver #")
        self.driver.set_window_size(1366, 768, 0)
        self.driver.get(self.base_url)
