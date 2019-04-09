
from selenium.webdriver.common.by import By
from base.verifypage import VerifyPage


class ApplicantDetailsPage(VerifyPage):

    # Locators
    locators = {
        "header": ["((//h2)[1]/following::div)[7]", "xpath"],
        "first_name": ["//label[contains(text(),'Legal First Name')]/following::input[1]", "xpath"],
        "preferred_name": ["//label[contains(text(),'Preferred First Name')]/following::input[1]", "xpath"],
        "middle_name": ["//label[contains(text(),'Middle Name')]/following::input[1]", "xpath"],
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
        "id_option": ["//label[contains(text(),'Identification Options')]/following::input[1]", "xpath"],
        "id_number": ["//label[contains(text(),'Identification Number')]/following::input[1]", "xpath"],
        "travel_id_option": ["//label[contains(text(),'Travel Identification Options')]/following::input[1]",
                             "xpath"],
        "travel_id_number": ["//label[contains(text(),'Travel Identification Number')]/following::input[1]",
                             "xpath"],
        "save_continue_button": ['//button[contains(text(),"Save and Continue")]', "xpath"],
        "previous_button": ["//button[contains(text(),'Previous')]", "xpath"]
    }

    def enter_first_name(self, first_name):
        self.send_keys(first_name, self.locators["first_name"])

    def enter_preferred_name(self, preferred_name):
        self.send_keys(preferred_name, self.locators["preferred_name"])

    def enter_middle_name(self, middle_name):
        self.send_keys(middle_name, self.locators["middle_name"])

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self.locators["last_name"])

    def enter_street(self, street):
        self.send_keys(street, self.locators["street"])

    def enter_city(self, city):
        self.send_keys(city, self.locators["city"])

    def enter_zip_code(self, zip_code):
        self.send_keys(zip_code, self.locators["zip_code"])

    def enter_cell(self, cell):
        self.send_keys(cell, self.locators["cell"])

    def enter_email(self, email):
        self.send_keys(email, self.locators["email"])

    def enter_country(self, country):

        # Refactor as base dropdown selection method
        self.click_element(self.locators["country"])
        country_element = self.driver.find_element(By.XPATH, f'//*[@title="{country}"]')
        country_element.click()

    def enter_state(self, state):

        # Refactor as base dropdown selection method
        self.click_element(self.locators["state"])
        state_element = self.driver.find_element(By.XPATH, f'//*[@title="{state}"]')
        state_element.click()

    def enter_birth_date(self, birth_date):
        self.send_keys(birth_date, self.locators["birth"])

    def enter_gender(self, gender):

        # Refactor as base dropdown selection method
        self.click_element(self.locators["gender"])
        gender_element = self.driver.find_element(By.XPATH, f'//*[@title="{gender}"]')
        gender_element.click()

    def enter_id_option(self, id_option):

        # Refactor as base dropdown selection method
        self.click_element(self.locators["id_option"])
        id_option_element = self.driver.find_element(By.XPATH, f'//*[@title="{id_option}"]')
        id_option_element.click()

    def enter_id_number(self, id_number):
        self.send_keys(id_number, self.locators["id_number"])

    def enter_travel_id_option(self, travel_id_option):

        # Refactor as base dropdown selection method
        self.click_element(self.locators["travel_id_option"])
        travel_id_option_element = self.driver.find_element(By.XPATH, f'(//*[@title="{travel_id_option}"])[2]')
        travel_id_option_element.click()

    def enter_travel_id_number(self, travel_id_number):
        self.send_keys(travel_id_number, self.locators["travel_id_number"])

    def click_save_continue_button(self):
        self.click_element(self.locators["save_continue_button"])

    def submit_applicant_details(self, **kwargs):

        # Refactor as verify page utility
        element = self.wait_for_element(self.locators["header"])
        header = element.text
        while header != "Applicant Details":
            self.click_element(self.locators["previous_button"])
            if header == "Applicant Details":
                break
