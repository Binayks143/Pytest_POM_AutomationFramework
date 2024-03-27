import unittest
from utilites.teststatus import TestStatus
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest
from ddt import ddt,data,unpack
@pytest.mark.usefixtures("oneTimeSetup","setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classsetup(self,oneTimeSetup):
        self.courses=RegisterCoursesPage(self.driver)
        self.ts=TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data (('JavaScript',370000000000002,1025,888,"India"),('rest',370000000000002,'0928',908,"China"))
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

