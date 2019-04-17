
import logging
from base.basepage import BasePage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginCommunityPage(BasePage):

    # Locators
    locators = {
        "email": ["//label[contains(text(),'Enter your email address to begin')]/following::input[1]", 'xpath'],
        "first_name": ["//label[contains(text(),'First Name')]/following::input[1]", "xpath"],
        "last_name": ["//label[contains(text(),'Last Name')]/following::input[1]", "xpath"],
        "password": ["//label[contains(text(),'Password')]/following::input[1]", "xpath"],
        "continue_button": ["//button[contains(text(),'Continue')]", "xpath"],
    }

    def enter_email(self, email):
        self.send_keys(email, self.locators["email"])

    def enter_first_name(self, first_name):
        self.send_keys(first_name, self.locators["first_name"])

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self.locators["last_name"])

    def enter_password(self, password):
        self.send_keys(password, self.locators["password"])

    def click_continue_button(self):
        self.click_element(self.locators["continue_button"])

    def login_community(self, **kwargs):
        self.wait_for_element(self.locators["email"])
        self.enter_email(kwargs.get('email'))
        self.click_continue_button()

        name_field_present = self.wait_for_element(self.locators["first_name"])
        try:
            if name_field_present:
                self.enter_first_name(kwargs.get('first_name'))
                self.enter_last_name(kwargs.get('last_name'))
                self.click_continue_button()
            else:
                self.wait_for_element(self.locators["password"])
                self.send_keys(kwargs.get('password'), self.locators["password"])
                self.click_continue_button()
        except:
            logging.info("# Element Not Found #")
