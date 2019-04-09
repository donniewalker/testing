
import logging
from base.seleniumdriver import SeleniumDriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class VerifyPage(SeleniumDriver):

    def verify_title(self):
        return self.driver.title

    # same design as the by.type static methods (refactor)
    def verify_user(self):
        name_field_present = self.wait_for_element(getattr(self, 'locators')['first_name'], timeout=1)
        try:
            if name_field_present:
                getattr(self, 'enter_first_name')(kwargs.get('first_name'))
                getattr(self, 'enter_last_name("last_name")')
                getattr(self, 'locators["click_continue_button"]')
            else:
                getattr(self, 'enter_password(kwargs.get("password"))')
                getattr(self, 'locators%s' % ['click_continue_button'])
        except:
            logging.info("# Element Not Found #")

    def verify_input(self):
        locators = getattr(self, 'locators.items()')
        for key, value in locators:
            element = self.get_element(value)
            user_value = element.get_attribute('value')
            try:
                input_field = getattr(self, 'kwargs%s' % [key])
                if user_value not in input_field:
                    enter_correct_value = getattr(self, 'enter_%s' % key)
                    enter_correct_value(input_field)
                else:
                    save_and_continue = getattr(self, 'click_save_continue_button')
                    save_and_continue()
            except:
                logging.info("# Define error message #")
