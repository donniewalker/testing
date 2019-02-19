"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""
import logging

from utilities.seleniumdriver import SeleniumDriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super(LoginPage, self).__init__(self.driver)
        self.driver = driver

    # Locators
    _username_field = "username"
    _password_field = "password"
    _login_button = "Login"

    def clearFields(self):
        usernameField = self.getElement(locator=self._username_field)
        usernameField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def enterUsername(self, username):
        self.sendKeys(username, self._username_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, username="", password=""):
        self.clearFields()
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("####")

    def logout(self):
        self.nav.navigateToSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath")
