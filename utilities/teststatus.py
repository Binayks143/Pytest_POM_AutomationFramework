"""
This class is designed to provide methods for marking and tracking test case results,
logging them appropriately, and handling failures in a test suite.
It integrates with Selenium WebDriver functionality inherited from the SeleniumDriver superclass.
"""

"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from traceback import print_stack

from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl
class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self,driver):
        """
        Init CHeckPoint class
        """
        super(TestStatus,self).__init__(driver)
        self.resultList=[]  #keep track all the results

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append('PASS')
                    self.log.info("### VERIFICATION SUCCESSFUL : "+ resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :" + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :"+ resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Some exception occurred")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self,result,resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result,resultMessage)

    def markFinal(self,testName,result,resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result,resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName +"Test case Failed !!!!")
            self.resultList.clear()
            assert True==False
            # intentionally failing the test case because if any one test case will fail all test case will be failed.
        else:
            self.log.info(testName+"Test Case Passed")
            self.resultList.clear()
            assert True==True








