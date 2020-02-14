"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from base.webdriver import WebDriver
from pages.formpage.jointformpage import JointFormPage
from pages.navigationpage.navigationpage import NavigationPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FormMultiPropertyPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.initiate_webdriver()
        cls.driver = cls.webdriver_instance.driver
        cls.user = NavigationPage(cls.driver)

    def test_one_submit_multi_property_form(self):
        logging.info("##### BEGIN SUBMIT MULTI-PROPERTY FORM #####")
        self.user.navigate_joint_form()
        prospect = JointFormPage(self.driver)
        prospect.submit_form(first_name="Jennifer", preferred_name="J", last_name="Houston", country="United States",
                             street="500 Main St", city="Victory", state="Alabama", zip_code="76543", cell="5123456789",
                             email="jenniferhouston@mailinator.com", gender="Female", in_the_fall_of="2019",
                             i_will_be_a="Freshman", describes_you="I am an incoming Freshman", housing="Yes",
                             hear_about_us="Social Media", travel_id_option="I Do Not Have One", travel_id_number="")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            # cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
