"""
Overall, this class provides a comprehensive set of methods for interacting with web elements
and performing actions required for web automation testing using Selenium WebDriver.
"""

import traceback
from selenium.webdriver.common.by import By
from traceback import print_stack

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():
    log=cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        return self.driver.title

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = str(resultMessage) + "_" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except Exception as e:
            self.log.error("###Error occurred while saving the screen shot %s" %str(e))
            print_stack()


    def getByType(self,locatorType):
        locatorType=locatorType.lower()

        if locatorType=="id":
            return By.ID
        elif locatorType=="name":
            return By.NAME
        elif locatorType=="classname":
            return By.CLASS_NAME
        elif locatorType=="css":
            return By.CSS_SELECTOR
        elif locatorType=="xpath":
            return By.XPATH
        elif locatorType=="linktext":
            return By.LINK_TEXT
        elif locatorType=="partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locatorType=="tagname":
            return By.TAG_NAME
        else:
            self.log.info(f"'{locatorType}' is not a Valid Locator")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f"Sent data={data} on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info(f"Cannot send data={data} on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def sendKeysWhenReady(self, data, locator="", locatorType="id"):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(10) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=10,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field so i will try to send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element_list = self.getElementList(locator, locatorType)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element is not avaialble on page")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType=self.getByType(locatorType)
            self.log.info(f"waiting for maximum {timeout} second for element to clickable")
            wait=WebDriverWait(self.driver,timeout=timeout,poll_frequency=pollFrequency,
                               ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   NoSuchFrameException
                                                   ])
            element=wait.until(EC.element_to_be_clickable((byType,locator)))
            self.log.info("Element Appeared on the webpage")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def webScroll(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 800);")

    def switchFrameByIndex(self, locator, locatorType="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: "+str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.elementPresenceCheck(locator, locatorType)
                if result:
                    self.log.info("iframe found in the webpage and index is:" + str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            self.log.info("iFrame index not found in the webpage")
            return result

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
            self.log.info("Switch frame with id: " + str(id))
        if name:
            self.driver.switch_to.frame(name)
            self.log.info("Switch frame with name: " + str(name))
        if index:
            self.log.info("Switch frame with index: " + str(index))
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content
        """
        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def selectDropdownOption(self, locator="", locatorType="id", element=None,option="value",optionData=""):

        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the dropdown element with locator: " + locator +
                          "and locatorType: " + locatorType)
            sel=Select(element)
            if option=="visibleText":
                sel.select_by_visible_text(optionData)
                self.log.info(f"Selected dropdown option with given visible_text='{optionData}'")
            elif option=="index":
                sel.select_by_index(int(optionData))
                self.log.info(f"Selected dropdown option with given index='{optionData}'")

            elif option=="value":
                sel.select_by_value(optionData)
                self.log.info(f"Selected dropdown option with given value='{optionData}'")

        except:
            self.log.info("Cannot click on dropdown element the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def windowSwitch(self):
        # Find parent handle -> Main Window
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent Handle: " + parentHandle)

        # Find all handles, there should two handles after clicking open window button
        handles = self.driver.window_handles

        # Switch to window and search course
        for handle in handles:
            self.log.info("Current New window Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                self.log.info("Switched to window:: " + handle)
                time.sleep(2)
                # self.driver.close()
                break