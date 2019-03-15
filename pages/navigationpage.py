"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Mar-13
"""

import logging

from tests.base import SeleniumDriver

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class NavigationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_form(self):
        logging.info("# Navigating to the Form page #")
        property_page = self.wait_for_element(locator="//*[@id='oneHeader']//a/span[1][contains(text(),"
                                                           "'Properties')]", locator_type="xpath", pollFrequency=1)
        self.click_element(locator="", locator_type="", element=property_page)
        properties_element = self.wait_for_element(locator="679", locator_type="partial_link", pollFrequency=1)
        self.click_element(locator="", locator_type="", element=properties_element)
        form_element = self.wait_for_element(locator="//a[contains(@href,'https://sandbox-efficiency-page-"
                                                           "8761-1694a6059cf.cs69.force.com/s/guest-card?moc="
                                                           "On_Site&propertyId=a1B2D0000003JtUUAU&pNum=679')]",
                                                           locator_type="xpath", pollFrequency=1)
        window_before = self.driver.window_handles[0]
        print(window_before)
        self.click_element(locator="", locator_type="", element=form_element)
        self.wait_for_element(locator="input-2", locator_type="id", pollFrequency=1)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        print(window_after)
