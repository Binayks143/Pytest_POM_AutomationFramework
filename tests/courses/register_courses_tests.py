import unittest
from utilites.teststatus import TestStatus
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetup","setUp")
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classetup(self,oneTimeSetup):
        self.courses=RegisterCoursesPage(self.driver)
        self.ts=TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enrollCourse(name="JavaScript",cn=6767654456667345,ed=1025,cvv=888)
        result=self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

