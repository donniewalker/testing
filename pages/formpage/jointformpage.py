
from base.seleniumdriver import SeleniumDriver


class JointFormPage(SeleniumDriver):

    # Locators
    locators = {
        "first_name": ["//label[contains(text(),'Legal First Name')]/following::input[1]", "xpath"],
        "preferred_name": ["//label[contains(text(),'Preferred First Name')]/following::input[1]", "xpath"],
        "last_name": ["//label[contains(text(),'Last Name')]/following::input[1]", "xpath"],
        "street": ["(//label[contains(text(),'Street')]/following::textarea)[1]", "xpath"],
        "city": ["//label[contains(text(),'City')]/following::input[1]", "xpath"],
        "zip_code": ["//label[contains(text(),'Zip')]/following::input[1]", "xpath"],
        "email": ["//label[contains(text(),'Email')]/following::input[1]", "xpath"],
        "cell": ["//label[contains(text(),'Cell')]/following::input[1]", "xpath"],
        "birth_date": ["//label[contains(text(),'Birthdate')]/following::input[1]", "xpath"],
        "country": ["//label[contains(text(),'Country')]/following::input[1]", "xpath"],
        "state": ["//label[contains(text(),'State')]/following::input[1]", "xpath"],
        "gender": ["//label[contains(text(),'Gender')]/following::input[1]", "xpath"],
        "class": ["//label[contains(text(),'Class')]/following::input[1]", "xpath"],
        "description": ["//label[contains(text(),'Description')]/following::input[1]", "xpath"],
        "discovered": ["//label[contains(text(),'Discovered')]/following::input[1]", "xpath"],

    }

    def enter_first_name(self, first_name):
        self.send_keys(first_name, self.locators["first_name"])

    def enter_preferred_name(self, preferred_name):
        self.send_keys(preferred_name, self.locators["preferred_name"])

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self.locators["last_name"])

    def enter_street(self, street):
        self.send_keys(street, self.locators["street"])

    def enter_city(self, city):
        self.send_keys(city, self.locators["city"])

    def enter_zip_code(self, zip_code):
        self.send_keys(zip_code, self.locators["zip"])

    def enter_cell(self, cell):
        self.send_keys(cell, self.locators["cell"])

    def enter_email(self, email):
        self.send_keys(email, self.locators["email"])

    def enter_country(self):



    def enter_state(self):



    def enter_gender(self):



    def enter_birth_date(self):



    def enter_class(self):



    def enter_description(self):



    def enter_discovered(self):



    def enter_property_one(self):


    def enter_property_two(self):


    def enter_property_three(self):


    def enter_housing(self):


    def enter_text_opt_in(self):


    def click_submit(self):


    def submit_form(self):


    def submit_partial_form(self):
        pass

