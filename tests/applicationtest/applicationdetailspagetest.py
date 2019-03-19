"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from utilities.webdriver import WebDriver
from pages.applicationpage.applicantdetailspage import ApplicantDetailsPage
from tests.logintest.logincommunitypagetest import LoginCommunityPage
from pages.navigationpage import NavigationPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ApplicantDetailsPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.get_webdriver_instance()
        cls.driver = cls.webdriver_instance.driver
        user = NavigationPage(cls.driver)
        user.navigate_to_communtiy_apply()
        new_applicant = LoginCommunityPage(cls.driver)
        new_applicant.community_apply("James@mercer.com", "James", "Mercer")

    def test_one_submit_applicant_details_form(self):
        logging.info("##### BEGIN SUBMIT APPLICANT DETAILS #####")
        prospect = ApplicantDetailsPage(self.driver)
        prospect.submit_applicant_details("Henry", "Hen", "Madison", "1234 Yorktown St", "New Hampshire", "67567",
                                          "3546789876", "henry@madison.com")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
