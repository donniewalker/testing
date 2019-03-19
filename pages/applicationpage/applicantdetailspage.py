"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

from utilities.seleniumdriver import SeleniumDriver
from selenium.webdriver.support.select import Select


class ApplicantDetailsPage(SeleniumDriver):

    # Locators
    _preferred_name = "input-41"
    _middle_name = "input-42"
    _street = "input-10"
    _city = "input-11"
    _zip_code = "input-13"
    _email = "input-44"
    _cell = "input-49"

    # Locator types
    _preferred_name_type = "id"
    _middle_name_type = "id"
    _street_type = "id"
    _city_type = "id"
    _zip_code_type = "id"
    _cell_type = "id"
    _email_type = "id"

    def clear_fields(self):
        self.wait_for_element(self._email, self._email_type)
        self.clear_field(self._email, self._email_type)

    def enter_preferred_name(self, preferred_name):
        self.send_keys(preferred_name, self._preferred_name, self._preferred_name_type)

    def enter_middle_name(self, middle_name):
        self.send_keys(middle_name, self._middle_name, self._middle_name_type)

    def enter_street(self, street):
        self.send_keys(street, self._street, self._street_type)

    def enter_city(self, city):
        self.send_keys(city, self._city, self._city_type)

    def enter_zip_code(self, zip_code):
        self.send_keys(zip_code, self._zip_code, self._zip_code_type)

    def enter_cell(self, cell):
        self.send_keys(cell, self._cell, self._cell_type)

    def enter_email(self, email):
        self.send_keys(email, self._email, self._email_type)

    def select_country(self):
        self.click_element(locator="input-28", locator_type="id")
        self.click_element(locator="input-28-0-28", locator_type="id")

    def select_state(self):
        self.click_element(locator="input-31", locator_type="id")
        self.click_element(locator="input-31-4-31", locator_type="id")

    def select_birth_date(self):
        self.click_element(locator="input-46", locator_type="id")
        self.click_element(locator="select-element-68", locator_type="id")
        year_element = self.get_element(locator="input-31-4-31", locator_type="id")
        birth_value = Select(year_element)
        birth_value.select_by_value("2000")

    def select_gender(self):
        self.click_element(locator="input-55", locator_type="id")
        self.click_element(locator="input-55-2-5", locator_type="id")

    def select_id_option(self):
        self.click_element(locator="input-60", locator_type="id")
        self.click_element(locator="60-1-60", locator_type="id")

    def enter_id_option(self, ssn):
        self.send_keys(ssn, locator="input-51", locator_type="id")

    def select_travel_id_option(self):
        self.click_element(locator="input-65", locator_type="id")
        self.click_element(locator="65-0-65", locator_type="id")

    def click_continue(self):
        self.click_element(locator="//button[contains(text(),'Save and Continue')]", locator_type="xpath")

    def submit_applicant_details(self, preferred_name, middle_name, street, city, zip_code, cell,
                          email, ssn):
        self.clear_fields()
        self.enter_preferred_name(preferred_name)
        self.enter_middle_name(middle_name)
        self.select_country()
        self.enter_street(street)
        self.enter_city(city)
        self.select_state()
        self.enter_zip_code(zip_code)
        self.enter_cell(cell)
        self.enter_email(email)
        self.select_birth_date()
        self.select_gender()
        self.select_id_option()
        self.enter_id_option(ssn)
        self.select_travel_id_option()
        self.click_continue()

