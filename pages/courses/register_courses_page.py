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
    __searchTextBox="search"    #id
    __searchIcon="find-course search-course" # classname
    __courseName="//h4[contains(text(),'JavaScript for beginners')]"  #xpath
    __enrollButton='//button[contains(text(),"Enroll in Course")]'   #xpath
    __cardNumber="cardnumber"  #name
    __cardExpiryDate="exp-date"   #name
    __cardCVV="cvc"   #name
    __countryNameDropdown="form-control country-list"   #classname
    __countryName="Australia"
    __buyButton='(//button[@type="button"])[5]' #xpath
    __errorMessage="//p[@class='dynamic-text']/text()[contains(., 'Your card number is incorrect')]" #xpath


    def clickAllCourses(self):
        self.elementClick(self.__allCourses,"xpath")

    def enterCourseName(self,CourseName):
        self.sendKeys(CourseName,self.__searchTextBox)

    def clickSearchIcon(self):
        self.elementClick(self.__searchIcon,'classname')

    def clickCourse(self):
        self.elementClick(self.__courseName,"xpath")

    def clickOnEnrollButton(self):
        self.elementClick(self.__enrollButton,"xpath")

    def enterCardDetails(self,cardNum):
        self.sendKeys(cardNum,self.__cardNumber,'classname')

    def enterCardExpiry(self,cardExpiry):
        self.sendKeys(cardExpiry,self.__cardExpiryDate,"classname")

    def enterCvvDetails(self,CardCvv):
        self.sendKeys(CardCvv,self.__cardCVV,"classname")

    def enterCreditCardInformation(self,cardNum,cardExpiryDate,cardCvv):
        self.enterCardDetails(cardNum)
        self.enterCardExpiry(cardExpiryDate)
        self.enterCvvDetails(cardCvv)


    def selectCountry(self):
        self.elementClick(self.__countryNameDropdown,"classname")

    def clickBuyButton(self):
        self.elementClick(self.__buyButton,"xpath")

    def enrollCourse(self,name,cn,ed,cvv):
        self.clickAllCourses()
        self.enterCourseName(name)
        self.clickSearchIcon()
        self.clickCourse()
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(cn,ed,cvv)
        self.clickBuyButton()

    def verifyEnrollFailed(self):
        messageElement=self.waitForElement(self.__errorMessage,"xpath")
        result=self.isElementDisplayed(element=messageElement)
        return result














