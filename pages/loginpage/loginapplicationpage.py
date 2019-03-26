"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

from utilities.seleniumdriver import SeleniumDriver
from pages.navigationpage import NavigationPage


class LoginApplicationPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.nav = NavigationPage(self.driver)

    # Locators
    locators = {
        "email_locator": ["input-2", 'id'],
        "first_name_locator": ["input-41", "id"],
        "last_name_locator": ["input-4", "id"],
        "password_locator": ["input-3", "id"],
        "continue_button_locator": ["//button[contains(text(),'Continue')]", "xpath"],
    }

    def enter_email(self, email):
        self.wait_for_element(self.locators["email_locator"])
        self.send_keys(email, self.locators["email_locator"])

    def enter_first_name(self, first_name):
        self.wait_for_element(self.locators["first_name_locator"])
        self.send_keys(first_name, self.locators["first_name_locator"])

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self.locators["last_name_locator"])

    def enter_password(self, password):
        self.send_keys(password, self.locators["password_locator"])

    def click_continue_button(self):
        self.click_element(self.locators["continue_button_locator"])

    def community_apply(self, email, first_name, last_name):
        self.enter_email(email)
        self.click_continue_button()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.click_continue_button()

    def community_apply_returning(self, email, password):
        self.enter_email(email)
        self.click_continue_button()
        self.wait_for_element(self.locators["password_locator"])
        self.send_keys(password, self.locators["password_locator"])
        self.click_continue_button()

    def community_resident(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_continue_button()


