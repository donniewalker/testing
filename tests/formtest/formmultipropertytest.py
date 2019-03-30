"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from base.webdriver import WebDriver
from pages.formpage.formmultipropertypage import FormMultiPropertyPage
from pages.navigationpage import NavigationPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FormMultiPropertyPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.get_webdriver_instance()
        cls.driver = cls.webdriver_instance.driver
        user = NavigationPage(cls.driver)
        user.navigate_to_multi_property_form()

    def test_one_submit_multi_property_form(self):
        logging.info("##### BEGIN SUBMIT MULTI-PROPERTY FORM #####")
        prospect = FormMultiPropertyPage(self.driver)
        prospect.submit_multi_property_form("Edgar", "Ed", "Santana", "1234 Yorktown St", "New Hampshire", "67567",
                                            "3546789876", "edgars@santanas.com")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
