"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import time

from base.seleniumdriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    # Locators
    _username_locator = "username"
    _password_locator = "password"
    _login_button_locator = "Login"
    _profile_locator = "//span[1]/span/img"
    _error_locator = "error"
    _logout_locator = "//div/a[2][contains(text(),'Log Out')]"

    # Locator Types
    _username_locator_type = "id"
    _password_locator_type = "id"
    _login_locator_type = "id"
    _profile_locator_type = "xpath"
    _error_locator_type = "id"
    _logout_locator_type = "xpath"

    def clear_fields(self):
        self.clear_field(self._username_locator, self._username_locator_type)
        self.clear_field(self._password_locator, self._password_locator_type)

    def enter_username(self, username):
        self.send_keys(username, self._username_locator, self._username_locator_type)

    def enter_password(self, password):
        self.send_keys(password, self._password_locator, self._password_locator_type)

    def click_login_button(self):
        self.click_element(self._login_button_locator, self._login_locator_type)

    def login_page(self, username, password):
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_valid(self):
        self.wait_for_element(self._profile_locator, self._profile_locator_type)
        result = self.is_element_present(self._profile_locator, self._profile_locator_type)
        return result

    def invalid_login_page(self, username, password):
        time.sleep(3)
        self.click_element(self._profile_locator, self._profile_locator_type)
        time.sleep(3)
        self.click_element(self._logout_locator, self._logout_locator_type)
        time.sleep(3)
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_invalid(self):
        self.wait_for_element(self._error_locator, self._error_locator_type)
        result = self.get_text(self._error_locator, self._error_locator_type)
        return result
