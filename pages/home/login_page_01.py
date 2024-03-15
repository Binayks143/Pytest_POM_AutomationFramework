
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver=driver

    #locators
    _signin_link="//a[contains(text(),'Sign In')]"
    _email_field="email"
    _password_field="login-password"
    _login_button="//button[@value='Login']"


    def getLoginLink(self):
        return self.driver.find_element(By.XPATH,self._signin_link)

    def getUserName(self):
        return self.driver.find_element(By.ID,self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID,self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH,self._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterUserName(self,username):
        self.getUserName().send_keys(username)

    def enterPassword(self,password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()


    def login(self,username,password):
        self.clickLoginLink()
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()
