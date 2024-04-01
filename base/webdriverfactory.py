"""
Overall, this class provides a simple factory method (getWebDriverInstance) to create instances of
Selenium WebDriver for different web browsers,
with common configurations such as implicit waits, window maximization, and navigation to a base URL.
"""


"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

'''
#old FLOW
from selenium import webdriver
class WebDriverFactory():
    def __init__(self,browser):
        self.browser=browser


#Set chrome driver and iexplorer environment based on OS
#PREFERRED: Set the path on the machine where browser will be executed


    def getWebDriverInstance(self):
        baseurl = "https://www.letskodeit.com/"

        if self.browser=="ie":
            driver=webdriver.Ie()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        elif self.browser=="chrome":
            driver=webdriver.Chrome()
        else:
            driver=webdriver.Chrome()

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseurl)
        return driver
'''



#### NEW CODE USEING WEBDRIVER MANAGER

"""
WebDriver Manager is a tool that helps automate the management of WebDriver binaries 
(like ChromeDriver, GeckoDriver, etc.) required by Selenium WebDriver. 
It can automatically download the required WebDriver binary for the specific browser 
version being used, and ensures that the WebDriver binary is available and up-to-date.
"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseurl = "https://www.letskodeit.com/"

        if self.browser == "ie":
            driver = webdriver.Edge()
        elif self.browser == "firefox":
            GeckoDriverManager().install()
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            ChromeDriverManager().install()
            driver = webdriver.Chrome()
        elif self.browser == "edge":
            EdgeChromiumDriverManager().install()
            driver = webdriver.Edge()
        else:
            ChromeDriverManager().install()
            driver = webdriver.Chrome()

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(baseurl)
        return driver
