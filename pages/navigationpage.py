from base.seleniumdriver import SeleniumDriver

class NavigationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _accounts = "Accounts"
    _prospects = "Prospects"
    _properties = "Properties"
    _applications = "Applications"
    _cases = "Cases"
    _leases = "Leases"
    _assignments = "Assignments"
    _setup = "Setup"
    _user_settings_icon = "//a[@class='menuTriggerLink slds-button slds-button_icon slds-button_icon slds-button_icon-container slds-button_icon-small slds-global-header__button_icon']"
    _logout = "Logout"

    def navigateToAccounts(self):
        self.elementClick(locator=self._accounts, locatorType="link")

    def navigateToProspects(self):
        self.elementClick(locator=self._prospects, locatorType="link")

    def navigateToProperties(self):
        self.elementClick(locator=self._properties, locatorType="link")

    def navigateToApplications(self):
        self.elementClick(locator=self._applications, locatorType="link")

    def navigateToCases(self):
        self.elementClick(locator=self._cases, locatorType="link")

    def navigateToLeases(self):
        self.elementClick(locator=self._leases, locatorType="link")

    def navigateToAssignments(self):
        self.elementClick(locator=self._assignments, locatorType="link")

    def navigateToSettings(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="link")

    def navigateToSetup(self):
        self.elementClick(locator=self._setup, locatorType="link")

    def navigateToSettings(self):
        settingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        self.elementClick(element=settingsElement)
        self.elementClick(locator=self._user_settings_icon,
                                      locatorType="xpath")

    def navigateToLogout(self):
        self.elementClick(locator=self._logout, locatorType="link")