"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import traceback
from selenium import webdriver

class WebDriverFactory():
    def __init__(self,browser):
        self.browser=browser


#Set chrome driver and iexplorer environment based on OS
#PREFERRED: Set the path on the machine where browser will be executed


    def getWebDriverInstance(self):
        baseurl = "https://www.letskodeit.com/"

        if self.browser=="ieexplorer":
            driver=webdriver.Ie()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        elif self.browser=="chrome":
            driver=webdriver.Chrome()
        else:
            driver=webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseurl)
        return driver


"""
Get WebDriver Instance based on the browser configuration
       Returns:
       'WebDriver Instance'
"""



