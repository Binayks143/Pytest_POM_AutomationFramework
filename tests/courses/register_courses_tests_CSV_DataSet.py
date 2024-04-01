import unittest
from utilities.teststatus import TestStatus
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest
from ddt import ddt,data,unpack
from utilities.read_csv_data import getCSVData
@pytest.mark.usefixtures("oneTimeSetup","setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classsetup(self,oneTimeSetup):
        self.courses=RegisterCoursesPage(self.driver)
        self.ts=TestStatus(self.driver)

    filepath=r"C:\Binay\PyChamp\upmove_framework\externalFiles\coursesdata.csv"
    @pytest.mark.run(order=1)
    @data (*getCSVData(filepath))
    @unpack
    def test_invalidEnrollment(self,courseName,cardNo,cardExpDate,cardCVV,country):

        self.courses.enrollCourse(course_name=courseName,card_no=cardNo,expiry_date=cardExpDate,cvv=cardCVV,countryName=country)
        result=self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
    @pytest.mark.run(order=2)
    def test_improperExpiryDate(self):
        self.courses.enrollCourse(course_name="JavaScript", card_no=370000000000002, expiry_date=1022, cvv=888,countryName="India")
        result = self.courses.verifyButtonEnabled()
        self.ts.markFinal("test_improperExpiryDate", result, "ExpiryDate validation")

