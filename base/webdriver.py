from selenium import webdriver

class WebDriverInstance():

    def getWebDriverInstance(self):
        driver = self.driver
        baseURL = "https://test.salesforce.com"
        # Instantiate webdriver
        driver = webdriver.Chrome()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver