import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home_icon="//a[@class='navbar-brand navbar-logo text-blue']"    #xpath
    _home="HOME"                            #link
    _all_courses = "All Courses"            #link
    _interview="INTERVIEW"                  #link
    _support="SUPPORT"                      #link
    _blog="BLOG"                            #link
    _pratice="PRACTICE"                     #link
    _my_courses = "My Courses"              #link
    _user_icon = "dropdownMenu1"            #ID


    def clickOnHomeIcon(self):
        self.elementClick(locator=self._home_icon,locatorType='xpath')

    def naviagteToHomePage(self):
        self.elementClick(locator=self._home,locatorType="linktext")
    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="linktext")

    def navigateToInterview(self):
        self.elementClick(locator=self._interview, locatorType="linktext")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="linktext")

    def navigateToBlog(self):
        self.elementClick(locator=self._blog, locatorType="linktext")

    def navigateToPratice(self):
        self.elementClick(locator=self._pratice, locatorType="linktext")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="linktext")
    def navigateToUserIcon(self):
        userSettingsElement = self.waitForElement(locator=self._user_icon,
                                      locatorType="id", pollFrequency=1)
        self.elementClick(element=userSettingsElement)