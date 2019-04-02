
from base.seleniumdriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    locators = {
        "username": ["username", "id"],
        "password": ["password", "id"],
        "login": ["Login", "id"],
        "profile": ["//header//img[@title='User']", "xpath"],
        "error": ["error", "id"],
        "logout": ["Log Out", "link"]
    }

    def enter_username(self, username):
        self.send_keys(username, self.locators["username"])

    def enter_password(self, password):
        self.send_keys(password, self.locators["password"])

    def click_login_button(self):
        self.click_element(self.locators["login"])

    def valid_login(self, username, password):
        self.wait_for_element(self.locators["username"])
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_element(self.locators["profile"])
        result = self.is_element_present(self.locators["profile"])
        return result

    def invalid_login(self, username, password):
        self.click_element(self.locators["profile"])
        self.wait_for_element(self.locators["logout"])
        self.click_element(self.locators["logout"])
        self.wait_for_element(self.locators["username"])
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_element(self.locators["error"])
        result = self.get_text(self.locators["error"])
        return result
