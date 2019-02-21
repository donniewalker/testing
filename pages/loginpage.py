"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""
import logging

from utilities.webdriver import WebDriverInstance

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage(WebDriverInstance):
    def __init__(self, driver):
        super().__init__(driver)
        wdi = WebDriverInstance(driver)
        self.driver = wdi.getWebDriverInstance()

    def enterUsername(self):
        self.driver.find_element_by_id("username").click()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("test-ug6swfcwdsa5@example.com")

    def enterPassword(self):
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("28)Gg#kH|G")

    def clickLoginButton(self):
        self.driver.find_element_by_id("Login").click()

    def login(self):
        self.enterUsername()
        self.enterPassword()
        self.clickLoginButton()

    def quit(self):
        self.driver.quit()

    # def verifyLoginSuccessful(self):
    #     self.waitForElement("//div[@id='navbar']//li[@class='dropdown']",
    #                                    locatorType="xpath")
    #     result = self.isElementPresent(locator="//div[@id='navbar']//li[@class='dropdown']",
    #                                    locatorType="xpath")
    #     return result
    #
    # def verifyLoginFailed(self):
    #     result = self.isElementPresent(locator="//div[contains(text(),'Invalid email or password')]",
    #                                    locatorType="xpath")
    #     return result
    #
    # def verifyLoginTitle(self):
    #     return self.verifyPageTitle("####")
    #
    # def logout(self):
    #     self.nav.navigateToSettings()
    #     logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
    #                       locatorType="xpath", pollFrequency=1)
    #     self.elementClick(element=logoutLinkElement)
    #     self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
    #                       locatorType="xpath")