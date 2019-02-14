from pages.internal_user.navigation import navigation_page
from base.webdriver import webdriver

class LoginPage(webdriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = navigation_page(driver)

    # Locators
    _login_link = "https://test.salesforce.com"
    _username_field = "test-ug6swfcwdsa5@example.com"
    _password_field = "28)Gg#kH|G"
    _login_button = "Login"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="id")

    def enterEmail(self, email):
        self.sendKeys(email, self._username_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
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
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._username_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
