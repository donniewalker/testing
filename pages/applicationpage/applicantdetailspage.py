"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

from utilities.seleniumdriver import SeleniumDriver
from selenium.webdriver.common.by import By


class ApplicantDetailsPage(SeleniumDriver):

    # Locators
    text_locators = {
        "header": ["((//h2)[1]/following::div)[7]", "xpath"],
    }

    input_locators = {
        "first_name": ["//label[contains(text(),'Legal First Name')]/following::input[1]", "xpath"],
        "preferred_name": ["//label[contains(text(),'Preferred First Name')]/following::input[1]", "xpath"],
        "middle_name": ["//label[contains(text(),'Middle Name')]/following::input[1]", "xpath"],
        "last_name": ["//label[contains(text(),'Last Name')]/following::input[1]", "xpath"],
        "street": ["(//label[contains(text(),'Street')]/following::textarea)[1]", "xpath"],
        "city": ["//label[contains(text(),'City')]/following::input[1]", "xpath"],
        "zip_code": ["//label[contains(text(),'Zip')]/following::input[1]", "xpath"],
        "email": ["//label[contains(text(),'Email')]/following::input[1]", "xpath"],
        "cell": ["//label[contains(text(),'Cell')]/following::input[1]", "xpath"],
        "birth": ["//label[contains(text(),'Birthdate')]/following::input[1]", "xpath"],
        "country": ["//label[contains(text(),'Country')]/following::input[1]", "xpath"],
        "state": ["//label[contains(text(),'State')]/following::input[1]", "xpath"],
        "gender": ["//label[contains(text(),'Gender')]/following::input[1]", "xpath"],
        "id_option": ["//label[contains(text(),'Identification Options')]/following::input[1]", "xpath"],
        "id_number": ["//label[contains(text(),'Identification Number')]/following::input[1]", "xpath"],
        "travel_id_option": ["//label[contains(text(),'Travel Identification Options')]/following::input[1]",
                             "xpath"],
        "travel_id_number": ["//label[contains(text(),'Travel Identification Number')]/following::input[1]",
                             "xpath"],
    }

    button_locators = {
        "save_continue_button": ['//button[contains(text(),"Save and Continue")]', "xpath"],
        "previous_button": ["//button[contains(text(),'Previous')]", "xpath"]
    }

    def enter_first_name(self, first_name):
        self.send_keys(first_name, self.input_locators["first_name"])

    def enter_preferred_name(self, preferred_name):
        self.send_keys(preferred_name, self.input_locators["preferred_name"])

    def enter_middle_name(self, middle_name):
        self.send_keys(middle_name, self.input_locators["middle_name"])

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self.input_locators["last_name"])

    def enter_street(self, street):
        self.send_keys(street, self.input_locators["street"])

    def enter_city(self, city):
        self.send_keys(city, self.input_locators["city"])

    def enter_zip_code(self, zip_code):
        self.send_keys(zip_code, self.input_locators["zip_code"])

    def enter_cell(self, cell):
        self.send_keys(cell, self.input_locators["cell"])

    def enter_email(self, email):
        self.send_keys(email, self.input_locators["email"])

    def enter_country(self, country):
        self.click_element(self.input_locators["country"])
        country_element = self.driver.find_element(By.XPATH, f'//*[@title="{country}"]')
        country_element.click()

    def enter_state(self, state):
        self.click_element(self.input_locators["state"])
        state_element = self.driver.find_element(By.XPATH, f'//*[@title="{state}"]')
        state_element.click()

    def enter_birth_date(self, birth_date):
        self.send_keys(birth_date, self.input_locators["birth"])

    def enter_gender(self, gender):
        self.click_element(self.input_locators["gender"])
        gender_element = self.driver.find_element(By.XPATH, f'//*[@title="{gender}"]')
        gender_element.click()

    def enter_id_option(self, id_option):
        self.click_element(self.input_locators["id_option"])
        id_option_element = self.driver.find_element(By.XPATH, f'//*[@title="{id_option}"]')
        id_option_element.click()

    def enter_id_number(self, id_number):
        self.send_keys(id_number, self.input_locators["id_number"])

    def enter_travel_id_option(self, travel_id_option):
        self.click_element(self.input_locators["travel_id_option"])
        travel_id_option_element = self.driver.find_element(By.XPATH, f'(//*[@title="{travel_id_option}"])[2]')
        travel_id_option_element.click()

    def enter_travel_id_number(self, travel_id_number):
        self.send_keys(travel_id_number, self.input_locators["travel_id_number"])

    def click_save_continue_button(self):
        self.click_element(self.button_locators["save_continue_button"])

    def submit_applicant_details(self, first_name, preferred_name, middle_name, last_name, street, city, country, state,
                                 zip_code, cell, email, gender, birth_date, id_option, id_number,
                                 travel_id_option, travel_id_number):

        header = self.wait_for_element(self.text_locators["header"]).text
        while header != "Applicant Details":
            self.click_element(self.button_locators["previous_button"])
            if header == "Applicant Details":
                break
            else:
                break

        self.wait_for_element(self.input_locators["first_name"])

        for key, value in self.input_locators.items():
            element = self.get_element(value)
            user_input = element.get_attribute('value')
            if user_input not in (first_name, preferred_name, middle_name, last_name, street, city, country, state,
                                  zip_code, cell, email, gender, birth_date, id_option, id_number,
                                  travel_id_option, travel_id_number):
                self.enter_preferred_name(preferred_name)
            else:
                pass
        self.click_save_continue_button()
