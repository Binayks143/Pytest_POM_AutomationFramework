#Using selenium driver here for better structure of code.

import logging
import time
import utilites.custom_logger as cl
from base.basepage import BasePage

class LoginPage(BasePage):
    log=cl.customLogger(logging.DEBUG) #overwriting the selenium driver logs
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #locators
    _signin_link="//a[contains(text(),'Sign In')]"
    _email_field="email"
    _password_field="login-password"
    _login_button="//button[@value='Login']"
    _loginSuccessID="dropdownMenu1"
    _loginPageError="//span[contains(text(),'Incorrect login details. Please try again.')]"

    #using selenium driver page implemention
    def clickLoginLink(self):
        self.elementClick(self._signin_link,"xpath")

    def enterUserName(self,username):
        self.sendKeys(username,self._email_field)
        # by default id is there so locator type is not mandatory

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field,"ID")

    def clickLoginButton(self):
        self.elementClick(self._login_button,"xpath")
        time.sleep(3)

    def clearFields(self):
        emailField=self.getElement(self._email_field)
        emailField.clear()

        passwordField=self.getElement(self._password_field)
        passwordField.clear()


    def varifyLoginSuccessful(self):
        result=self.isElementPresent(self._loginSuccessID,locatorType="id")
        return result

    def varifyInvalidLogin(self):
        result=self.isElementPresent(self._loginPageError,locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        #print("TITLE="+self.getTitle())
        return self.verifyPageTitle("My Courses")

    def login(self,username="",password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterUserName(username)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()
        time.sleep(2)

