"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_by_type(locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            logging.info("# Locator Type Not Supported #")

    def get_element(self, locator, locator_type):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            logging.info("# Element found #")
        except:
            logging.info("# Element not found #")

        return element

    def get_title(self):
        return self.driver.title

    def get_text(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element = element.text
            logging.info("# Text found on element #")
        except:
            logging.info("# Text not found on element #")
        return element

    def click_element(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            logging.info("# Clicking on element #")
        except:
            logging.info("# Element not found #")

    def clear_field(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            element.clear()
            logging.info("# Clearing field #")
        except:
            logging.info("# Element not found #")

    def send_keys(self, data, locator, locator_type):
        try:
            if locator:
                by_type = self.get_by_type(locator_type)
                element = self.driver.find_element(by_type, locator)
                element.send_keys(data)
                logging.info("# Entering data #")
        except:
            logging.info("# Element not found #")

    def is_element_present(self, locator, locator_type, element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                logging.info("# Element is present")
                return True
            else:
                logging.info("# Element not present with locator #")
                return False
        except:
            logging.info("# Element not found #")
            return False

    def wait_for_element(self, locator, locator_type,
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            logging.info("# Waiting for element to become clickable #")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            logging.info("# Element found #")
        except:
            logging.info("# Element not found #")
        return element
