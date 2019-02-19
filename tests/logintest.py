"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-19
"""

from pages.loginpage import LoginPage
from utilities.webdriverinstance import WebdriverInstance


class LoginTests(WebdriverInstance):
    def test_oneValidLogin(self):
        login_page = LoginPage(self.driver)
        login_page.login("test-ug6swfcwdsa5@example.com", "28)Gg#kH|G")
        # result = self.lp.verifyLogin Successful()
        # assert result == True