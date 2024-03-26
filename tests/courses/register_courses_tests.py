import unittest
from utilites.teststatus import TestStatus
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest

@pytest.mark.usefixtures("oneTimeSetup","setUp")
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classsetup(self,oneTimeSetup):
        self.courses=RegisterCoursesPage(self.driver)
        self.ts=TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enrollCourse(course_name="JavaScript",card_no=370000000000002,expiry_date=1025,cvv=888,country="Austria")
        result=self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")

    @pytest.mark.run(order=2)
    def test_improperExpiryDate(self):
        self.courses.enrollCourse(course_name="JavaScript", card_no=370000000000002, expiry_date=1022, cvv=888,country="Austria")
        result = self.courses.verifyButtonEnabled()
        self.ts.markFinal("test_improperExpiryDate", result, "ExpiryDate validation")

