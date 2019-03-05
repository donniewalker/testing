"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

import logging
import time

from utilities.seleniumdriver import SeleniumDriver


from utilities.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginPage(SeleniumDriver):

    # Locators
    _username_locator = "username"
    _password_locator = "password"
    _login_button_locator = "Login"

    # Locator Types
    _username_locator_type = "id"
    _password_locator_type = "id"
    _login_locator_type = "id"

    def clear_fields(self):
        self.clear_field(self._username_locator, self._username_locator_type)
        self.clear_field(self._password_locator, self._password_locator_type)

    def enter_username(self, username):
        self.send_keys(username, self._username_locator, self._username_locator_type)

    def enter_password(self, password):
        self.send_keys(password, self._password_locator, self._password_locator_type)

    def click_login_button(self):
        self.click_element(self._login_button_locator, self._login_locator_type)

    def login(self, username, password):
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def loginSuccessful(self):
        wdi = WebDriver()
        self.driver = wdi.driver
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, "//*[@id='oneHeader']//img")
        element.click()
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5)
        user_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[1]/span/img")))
        try:
            if user_name is not None:
                return True
            else:
                return False
        except:
            print("Element Not Found")
            return False


