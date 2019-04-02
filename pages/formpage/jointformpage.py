
from base.seleniumdriver import SeleniumDriver


class JointFormPage(SeleniumDriver):

    # Locators
    _first_name = "input-2"
    _preferred_name = "input-3"
    _last_name = "input-4"
    _street = "input-6"
    _city = "input-7"
    _zip_code = "input-9"
    _cell = "input-10"
    _email = "input-11"

    # Locator types
    _first_name_type = "id"
    _preferred_name_type = "id"
    _last_name_type = "id"
    _street_type = "id"
    _city_type = "id"
    _zip_code_type = "id"
    _cell_type = "id"
    _email_type = "id"

    def enter_first_name(self, first_name):
        self.wait_for_element(self._first_name, self._first_name_type, pollFrequency=1)
        self.send_keys(first_name, self._first_name, self._first_name_type)

    def enter_preferred_name(self, preferred_name):
        self.send_keys(preferred_name, self._preferred_name, self._preferred_name_type)

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self._last_name, self._last_name_type)

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
        self.click_element(locator="input-25", locator_type="id")
        self.click_element(locator="input-25-0-25", locator_type="id")

    def select_state(self):
        self.click_element(locator="input-28", locator_type="id")
        self.click_element(locator="input-28-4-28", locator_type="id")

    def select_gender(self):
        self.click_element(locator="input-31", locator_type="id")
        self.click_element(locator="input-31-1-31", locator_type="id")

    def select_year(self):
        self.click_element(locator="input-34", locator_type="id")
        self.click_element(locator="input-34-0-34", locator_type="id")

    def select_class(self):
        self.click_element(locator="input-37", locator_type="id")
        self.click_element(locator="input-37-0-37", locator_type="id")

    def select_description(self):
        self.click_element(locator="input-40", locator_type="id")
        self.click_element(locator="input-40-0-40", locator_type="id")

    def select_discovered(self):
        self.click_element(locator="input-46", locator_type="id")
        self.click_element(locator="input-46-4-46", locator_type="id")

    def select_property_one(self):
        self.click_element(locator="checkbox-0-22", locator_type="id")

    def select_property_two(self):
        self.click_element(locator="checkbox-1-22", locator_type="id")

    def select_property_three(self):
        self.click_element(locator="checkbox-2-22", locator_type="id")

    def click_housing(self):
        self.click_element(locator="//*[@id='radio-0-20']/following-sibling::label", locator_type="xpath")

    def click_text_opt_in(self):
        self.click_element(locator="//*[@id='radio-0-24']/following-sibling::label", locator_type="xpath")
        self.click_element(locator="//span[contains(text(),'I AGREE TO THE ABOVE TERMS.')]/preceding-sibling::span",
                           locator_type="xpath")

    def click_submit(self):
        self.click_element(locator="//button[contains(text(),'Submit')]", locator_type="xpath")

    def submit_multi_property_form(self, first_name, preferred_name, last_name, street, city, zip_code, cell, email):
        self.enter_first_name(first_name)
        self.enter_preferred_name(preferred_name)
        self.enter_last_name(last_name)
        self.select_country()
        self.enter_street(street)
        self.enter_city(city)
        self.select_state()
        self.enter_zip_code(zip_code)
        self.enter_cell(cell)
        self.enter_email(email)
        self.select_gender()
        self.select_year()
        self.select_class()
        self.select_description()
        self.click_housing()
        self.select_discovered()
        self.select_property_one()
        self.select_property_two()
        self.select_property_three()
        self.click_text_opt_in()
        self.click_submit()

    def submit_form_partial(self):
        pass

