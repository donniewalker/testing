
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
    def get_by_type(locator):
        locator = locator.lower()
        if locator == "id":
            return By.ID
        elif locator == "name":
            return By.NAME
        elif locator == "xpath":
            return By.XPATH
        elif locator == "css":
            return By.CSS_SELECTOR
        elif locator == "class":
            return By.CLASS_NAME
        elif locator == "link":
            return By.LINK_TEXT
        elif locator == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            logging.info("# Locator Type Not Supported #")

    def get_element(self, locator):
        element = None
        try:
            by_type = self.get_by_type(locator[1])
            element = self.driver.find_element(by_type, locator[0])
            logging.info("# Element found #")
        except:
            logging.info("# Element not found #")

        return element

    def get_title(self):
        return self.driver.title

    def get_text(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            element = element.text
            logging.info("# Text found on element #")
        except:
            logging.info("# Text not found on element #")

        return element

    def click_element(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            element.click()
            logging.info("# Clicking on element #")
        except:
            logging.info("# Element not found #")

    def clear_field(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            element.click()
            element.clear()
            logging.info("# Clearing field #")
        except:
            logging.info("# Element not found #")

    def send_keys(self, data, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            element.click()
            element.clear()
            element.send_keys(data)
            logging.info("# Entering data #")
        except:
            logging.info("# Element not found #")

    def is_element_present(self, locator, element=None):
        try:
            if locator:
                element = self.get_element(locator)
            if element is not None:
                logging.info("# Element is present")
                return True
            else:
                logging.info("# Element not present with locator #")
                return False
        except:
            logging.info("# Element not found #")
            return False

    def wait_for_element(self, locator, timeout=10, pollFrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator[1])
            logging.info("# Waiting for element to become clickable #")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator[0])))
            logging.info("# Element found #")
        except:
            logging.info("# Element not found #")
        return element

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
