
import logging
from base.seleniumdriver import SeleniumDriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class BasePage(SeleniumDriver):

    def verify_title(self):
        return self.driver.title

    def verify_user(self, kwargs):
        name_field_present = self.wait_for_element(getattr(self, 'locators')['first_name'], timeout=1)
        try:
            if name_field_present:
                getattr(self, 'enter_first_name')(kwargs.get('first_name'))
                getattr(self, 'enter_last_name')(kwargs.get('last_name'))
                getattr(self, 'click_continue_button')()
            else:
                getattr(self, 'enter_password')(kwargs.get('password'))
                getattr(self, 'click_continue_button')()
        except:
            logging.info("# Element Not Found #")

    def verify_header(self, *args):
        element = self.wait_for_element(getattr(self, 'text_locators')["header"])
        header_present = element.text
        while header_present != args:
            self.click_element(getattr(self, 'button_locators')['previous_button'])
            if header_present:
                break

    def verify_input(self, kwargs):
        locators = getattr(self, 'locators')
        items = locators.items()
        for key, value in items:
            self.wait_for_element(getattr(self, 'locators')[key])
            element = self.get_element(value)
            user_value = element.get_attribute('value')
            input_field = kwargs[key]
            try:
                if user_value != input_field:
                    getattr(self, 'enter_%s' % key)(input_field)
                else:
                    continue
            except AttributeError:
                logging.info("Non Input Element")

        getattr(self, 'click_save_continue_button')()
