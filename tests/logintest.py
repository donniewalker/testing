import unittest
from base.webdriverinstance import WebDriverInstance
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class LoginTests(unittest.TestCase):
    def setUp(self):
        # self.base_url = "https://test.salesforce.com"
        # self.lp = LoginPage(self.driver)

    def test_oneValidLogin(self):
        # self.lp.login("test-ug6swfcwdsa5@example.com", "28)Gg#kH|G")
        # result = self.lp.verifyLogin Successful()
        # assert result == True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()