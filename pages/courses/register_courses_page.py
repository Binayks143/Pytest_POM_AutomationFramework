import time

from selenium.webdriver.support.select import Select

import utilites.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    #Locators:
    __allCourses="//a[contains(text(),'ALL COURSES')]"  #Xpath
    __searchTextBox="//input[@id='search']"    #Xpath
    __searchIcon="//button[@class='find-course search-course']" # xpath
    __courseName="//h4[@class='dynamic-heading']"  #xpath
    __enrollButton='//button[contains(text(),"Enroll in Course")]'   #xpath
    __cardNumber="//input[@placeholder='Card Number']"  #xpath
    __cardExpiryDate="//input[@name='exp-date']"   #xpath
    __cardCVV="//input[@name='cvc']"   #name
    __countryNameDropdown="country-list"   #name
    __countryName="Australia"
    __buyButton='(//button[@type="button"])[5]' #xpath
    __errorMessage="//div[@role='alert']//p[@class='dynamic-text']" #xpath

    def clickAllCourses(self):
        self.elementClick(self.__allCourses,"xpath")

    def enterCourseName(self,CourseName):
        self.sendKeys(CourseName,self.__searchTextBox,'xpath')

    def clickSearchIcon(self):
        self.elementClick(self.__searchIcon,'xpath')
        time.sleep(3)

    def clickCourse(self):
        self.elementClick(self.__courseName,"xpath")

    def clickOnEnrollButton(self):
        time.sleep(5)
        self.elementClick(self.__enrollButton,"xpath")

    def enterCardDetails(self,cardNum):
        time.sleep(6)
        self.switchFrameByIndex(self.__cardNumber,'xpath')
        self.sendKeys(cardNum,self.__cardNumber,'xpath')
        self.switchToDefaultContent()

    def enterCardExpiry(self,cardExpiry):
        self.switchFrameByIndex(self.__cardExpiryDate,'xpath')
        self.sendKeys(cardExpiry,self.__cardExpiryDate,"xpath")
        self.switchToDefaultContent()

    def enterCvvDetails(self,CardCvv):
        self.switchFrameByIndex(self.__cardCVV,'xpath')
        self.sendKeys(CardCvv,self.__cardCVV,"xpath")
        self.switchToDefaultContent()


    def enterCreditCardInformation(self,cardNum,cardExpiryDate,cardCvv):
        self.enterCardDetails(cardNum)
        self.enterCardExpiry(cardExpiryDate)
        self.enterCvvDetails(cardCvv)

    def selectCountry(self,countryName):
        self.selectDropdownOption(locator=self.__countryNameDropdown,locatorType='name',
                                  option="visibleText",optionData=countryName)
        time.sleep(2)

    def clickBuyButton(self):
        self.elementClick(self.__buyButton,"xpath")

    def enrollCourse(self,course_name,card_no,expiry_date,cvv,countryName):
        self.clickAllCourses()
        self.enterCourseName(course_name)
        self.clickSearchIcon()
        self.clickCourse()
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(card_no,expiry_date,cvv)
        self.selectCountry(countryName)

    def verifyEnrollFailed(self):
        self.clickBuyButton()
        messageElement=self.waitForElement(self.__errorMessage,"xpath")
        result=self.isElementDisplayed(element=messageElement)
        return result

    def verifyButtonEnabled(self):
        result=self.isEnabled(locator=self.__buyButton,locatorType="xpath",info="Buy Button")
        return not result
        #Returning opposite because we have to varified its a disabled.














