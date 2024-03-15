import time
import unittest
from pages.home.login_page_02 import LoginPage
import pytest
from utilites.teststatus import TestStatus

@pytest.mark.usefixtures("setUp","oneTimeSetup")
class LoginPageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetup):
        self.lp = LoginPage(self.driver)
        self.ts=TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("binayks143@yahoo.com","Binay123@")
        time.sleep(3)
        output1 = self.lp.verifyLoginTitle()
        #assert output1 == True
        self.ts.mark(output1,"Title is Incorrect")
        output2=self.lp.varifyLoginSuccessful()
        #assert output2==True

        self.ts.markFinal("TestValidLogin",output2,"Login was successful")


    @pytest.mark.run(order=1)
    def test_inValidLogin(self):
        self.lp.login("binayks143@yahoo.com","Binay1234@")
        output=self.lp.varifyInvalidLogin()
        assert output==True


