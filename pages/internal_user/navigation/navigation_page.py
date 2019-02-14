from base.webdriver import webdriver

class NavigationPage(webdriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _accounts = "Accounts"
    _applications = "Applications"
    _cases = "Cases"
    _leases = "Leases"
    _assignments = "assignments"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon,
                                      locatorType="xpath")