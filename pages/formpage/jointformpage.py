
from base.basepage import BasePage


class JointFormPage(BasePage):

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
        "in_the_fall_of": ["//label[contains(text(),'In the Fall of')]/following::input[1]", "xpath"],
        "i_will_be_a": ["//label[contains(text(),'I will be a')]/following::input[1]", "xpath"],
        "describes_you": ["//label[contains(text(),'What best describes you?')]/following::input[1]", "xpath"],
        "housing": ["//legend[contains(text(),'Are you still looking for housing?')]"
                    "/following::input[@value='YES']", "xpath"],
        "hear_about_us": ["//label[contains(text(),'How did you hear about us?')]/following::input[1]", "xpath"],
        "text_opt_in": ["//span[contains(text(),'I AGREE TO THE ABOVE TERMS.')]/preceding::span[1]", "xpath"],
        "submit": ["//button[contains(text(),'Submit')]", "xpath"]
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

    def enter_country(self, country):
        self.select_by_visible_text(country, self.locators["country"])

    def enter_state(self, state):
        self.select_by_visible_text(state, self.locators["state"])

    def enter_gender(self, gender):
        self.select_by_visible_text(gender, self.locators["gender"])

    def enter_birth_date(self, birth_date):
        self.select_by_visible_text(birth_date, self.locators["birth_date"])

    def enter_in_the_fall_of(self, in_the_fall_of):
        self.select_by_visible_text(in_the_fall_of, self.locators["in_the_fall_of"])

    def enter_i_will_be_a(self, i_will_be_a):
        self.select_by_visible_text(i_will_be_a, self.locators["i_will_be_a"])

    def enter_describes_you(self, describes_you):
        self.select_by_visible_text(describes_you, self.locators["describes_you"])

    def enter_hear_about_us(self, hear_about_us):
        self.select_by_visible_text(hear_about_us, self.locators["hear_about_us"])

    def enter_property(self):
        checkboxes = self.driver.find_element_by_xpath("//span[@class='slds-checkbox_faux']")
        for checkbox in checkboxes:
            checkbox.click()

    def enter_housing(self, housing):
        self.click_element(housing, self.locators["housing"])

    def enter_text_opt_in(self):
        self.click_element(self.locators["text_opt_in"])
        self.click_element(self.locators["text_opt_in_disclaimer"])

    def click_submit(self):
        self.click_element(self.locators["submit"])

    def submit_form(self, **kwargs):
        self.enter_first_name(kwargs)
        self.enter_preferred_name(kwargs)
        self.enter_last_name(kwargs)
        self.enter_street(kwargs)
        self.enter_city(kwargs)
        self.enter_zip_code(kwargs)
        self.enter_email(kwargs)
        self.enter_cell(kwargs)
        self.enter_birth_date(kwargs)
        self.enter_country(kwargs)
        self.enter_state(kwargs)
        self.enter_gender(kwargs)
        self.enter_in_the_fall_of(kwargs)
        self.enter_i_will_be_a(kwargs)
        self.enter_describes_you(kwargs)
        self.enter_housing(kwargs)
        self.enter_hear_about_us(kwargs)
        self.enter_text_opt_in(kwargs)
        self.click_submit()
