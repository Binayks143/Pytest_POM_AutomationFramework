from seleniumwire import webdriver

#from pages.home.login_page_01 import LoginPage
from pages.home.login_page_02 import LoginPage


class LoginPageTests():
    baseurl="https://www.letskodeit.com/"

    def validLogin(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get(self.baseurl)

        lp=LoginPage(driver)
        lp.login("binayks143@yahoo.com","Binay123@")

        output1=lp.varifyLoginSuccessful()
        assert output1==True

        driver.quit()

o1=LoginPageTests()
o1.validLogin()


