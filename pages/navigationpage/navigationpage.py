
import logging

from utilities.seleniumdriver import SeleniumDriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class NavigationPage(SeleniumDriver):

    def navigate_to_single_form(self):
        logging.info("# Navigating to the Single Property Form Page #")
        self.driver.get("https://sandbox-efficiency-page-8761-1694a6059cf.cs69.force.com/s/"
                        "guest-card?moc=On_Site&propertyId=a1B2D0000003JtUUAU&pNum=679")

    def navigate_to_joint_form(self):
        logging.info("# Navigating to the Multi-Property Form Page #")
        self.driver.get("https://sandbox-efficiency-page-8761-1694a6059cf.cs69.force.com/s/"
                        "guest-card?moc=On_Site&marketingProperties=679,677,489")

    def navigate_to_application(self):
        logging.info("# Navigating to the Online Application Page #")
        self.driver.get("https://sandbox-efficiency-page-8761-1694a6059cf.cs69.force.com/s/"
                        "login?startUrl=/s/application&pNum=679&propertyId=a1B2D0000003JtUUAU")

    def navigate_to_community(self):
        logging.info("# Navigating to the Community Home Page #")
        self.driver.get("https://sandbox-efficiency-page-8761-1694a6059cf.cs69.force.com/s/login?pNum=679")

