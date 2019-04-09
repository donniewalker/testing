
import logging

from base.seleniumdriver import SeleniumDriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class NavigationPage(SeleniumDriver):

    def navigate_single_form(self):
        logging.info("# Navigating to the Single Property Form Page #")
        self.driver.get("https://sandbox-customization-customization--169bbac5f27.cs94.force.com/s/guest-card?moc="
                        "On_Site&propertyId=a1D0R000001YF0UUAW&pNum=489")

    def navigate_joint_form(self):
        logging.info("# Navigating to the Multi-Property Form Page #")
        self.driver.get("https://sandbox-customization-customization--169bbac5f27.cs94.force.com/s/guest-card?"
                        "moc=On_Site&marketingProperties=489")

    def navigate_application(self):
        logging.info("# Navigating to the Online Application Page #")
        self.driver.get("https://sandbox-customization-customization--169bbac5f27.cs94.force.com/s/"
                        "login?startUrl=/s/application&pNum=489&propertyId=a1D0R000001YF0UUAW")

    def navigate_community(self):
        logging.info("# Navigating to the Community Home Page #")
        self.driver.get("https://sandbox-customization-customization--169bbac5f27.cs94.force.com/s/login?pNum=489")

