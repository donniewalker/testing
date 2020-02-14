import logging
import unittest

from base.webdriver import WebDriver
from pages.applicationpage.applicantdetailspage import ApplicantDetailsPage
from pages.loginpage.loginapplicationpage import LoginApplicationPage
from pages.navigationpage.navigationpage import NavigationPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ApplicantDetailsPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.initiate_webdriver()
        cls.driver = cls.webdriver_instance.driver

        cls.user = NavigationPage(cls.driver)
        cls.user.navigate_application()
        applicant = LoginApplicationPage(cls.driver)
        applicant.login_application(email="greg@mercer.com", password="WelcomeToSFDC2018!",
                                    first_name="Greg", last_name="Mercer")
        cls.prospect = ApplicantDetailsPage(cls.driver)

    def test_1_submit_successful(self):
        logging.info("##### BEGIN ENTER AND SUBMIT APPLICANT DETAILS #####")
        self.prospect.submit_applicant_details(first_name="Greg", preferred_name="GM", middle_name="Dean",
                                               last_name="Mercer", street="5674 Century Blvd", city="Solange",
                                               country="United States", state="Montana", zip_code="90789",
                                               cell="3104765488", email="dowalker@americancampus.com", gender="Male",
                                               birth_date="Mar 1, 2000", id_option="SSN", id_number="545347687",
                                               travel_id_option="I Do Not Have One", travel_id_number="")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        # if cls.driver is not None:
        #     logging.info("# Removing Webdriver #")
        #     cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
