from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver:

    def getWebDriverInstance(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "/Users/donniewalker/PycharmProjects/lib/chromedriver"
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        base_url = "https://test.salesforce.com"
        driver.implicitly_wait(3)
        driver.get(base_url)
        window_before = driver.window_handles[0]
        print(window_before)
        return driver

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
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            print("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            print("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            print("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)

    def clearField(self, locator="", locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.clear()
        print("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                print("Getting text on element :: " +  info)
                print("The text is :: '" + text + "'")
                text = text.strip()
        except:
            print("Failed to get text on element " + info)
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                print("Element not spresent with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                print("Element is displayed" )
            else:
                print("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                print("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False