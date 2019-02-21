"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""
import logging

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            logging.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            logging.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            logging.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            logging.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            logging.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            logging.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            logging.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def clearField(self, locator="", locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.clear()
        logging.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            logging.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            logging.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                logging.info("Getting text on element :: " +  info)
                logging.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            logging.info("Failed to get text on element " + info)
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                logging.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                logging.info("Element not spresent with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            logging.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                logging.info("Element is displayed" )
            else:
                logging.info("Element not displayed")
            return isDisplayed
        except:
            logging.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                logging.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                logging.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            logging.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            logging.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            logging.info("Element appeared on the web page")
        except:
            logging.info("Element not appeared on the web page")
        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    # def verifyPageTitle(self, titleToVerify):
    #     try:
    #         actualTitle = self.getTitle()
    #         return self.util.verifyTextContains(actualTitle, titleToVerify)
    #     except:
    #         logging.info("Failed to get page title")
    #         return False