"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

from base import SeleniumDriver
from pages.navigationpage import NavigationPage


class LoginCommunityPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(self.driver)

    # Locators
    _email_locator = "input-2"
    _first_name_locator = "input-3"
    _last_name_locator = "input-4"
    _password_locator = "password"
    _continue_button_locator = "//button[contains(text(),'Continue')]"

    # Locator Types
    _email_locator_type = "id"
    _first_name_locator_type = "id"
    _last_name_locator_type = "id"
    _password_locator_type = "id"
    _continue_button_locator_type = "xpath"

    def enter_email(self, email):
        self.wait_for_element(locator=self._email_locator, locator_type=self._email_locator_type, pollFrequency=1)
        self.send_keys(email, self._email_locator, self._email_locator_type)

    def enter_first_name(self, first_name):
        self.wait_for_element(locator=self._first_name_locator, locator_type=self._first_name_locator_type,
                              pollFrequency=1)
        self.send_keys(first_name, self._first_name_locator, self._first_name_locator_type)

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self._last_name_locator, self._last_name_locator_type)

    def enter_password(self, password):
        self.send_keys(password, self._password_locator, self._password_locator_type)

    def click_continue_button(self):
        self.click_element(self._continue_button_locator, self._continue_button_locator_type)

    def community_apply(self, email, first_name, last_name):
        self.nav.navigate_to_community_apply()
        self.enter_email(email)
        self.click_continue_button()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.click_continue_button()

    def community_apply_multiple(self, email):
        self.nav.navigate_to_community_apply()
        self.enter_email(email)
        self.click_continue_button()

    def community_resident(self, email, password):
        self.nav.navigate_to_community_resident()
        self.enter_email(email)
        self.enter_password(password)
        self.click_continue_button()


