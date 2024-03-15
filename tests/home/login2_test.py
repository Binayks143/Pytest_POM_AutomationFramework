import unittest

from seleniumwire import webdriver
from pages.home.login_page_02 import LoginPage
import pytest


class LoginPageTest(unittest.TestCase):
    baseurl="https://www.letskodeit.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseurl)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseurl)
        self.lp.login("binayks143@yahoo.com","Binay123@")
        output=self.lp.varifyLoginSuccessful()
        assert output==True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_inValidLogin(self):
        self.driver.get(self.baseurl)
        self.lp.login("binayks143@yahoo.com","Binay1234@")
        output=self.lp.varifyInvalidLogin()
        assert output==True


