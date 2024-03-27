import unittest
from tests.home.login3_test import LoginPageTests
from tests.courses.register_courses_tests import RegisterCoursesTests
from tests.courses.register_courses_tests_CSV_DataSet import RegisterCoursesCSVDataTests

# Get all the tests from the test classes
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginPageTests)
tc2=unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)
tc3=unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

#Creating a test suite combining all the test classes
smokeTest=unittest.TestSuite([tc1,tc2,tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)