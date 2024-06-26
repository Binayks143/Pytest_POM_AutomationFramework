#This is the default file name for pytest configuration
# when scope =module it will run only one time in the module
# example is in test_case_03.py
#scopr =session,class,module

"""
This code snippet seems to be related to setting up fixtures and options for pytest, a popular testing framework in Python. Let's break down what each part does:

def pytest_addoption(parser):

This function is a hook provided by pytest that allows you to define custom command-line options for your test suite.
parser is an instance of the Parser class provided by pytest, which is used to define command-line options.
In this function, two options are defined:
--browser: This option allows the user to specify which browser to use for testing.
--osType: This option allows the user to specify the type of operating system for testing.
@pytest.fixture(scope="session")

This is a decorator provided by pytest for defining fixtures, which are functions that provide data to your tests.
scope="session" indicates that the fixture will be instantiated only once per test session.
def browser(request):

This is a fixture function named browser which provides the value of the --browser option specified by the user.
request is a special fixture provided by pytest that gives access to information and functionality regarding the current test run.
request.config.getoption("--browser") retrieves the value of the --browser option provided by the user via the command line.
def osType(request):

This is another fixture function named osType which provides the value of the --osType option specified by the user.
Similar to the browser fixture, it retrieves the value of the --osType option using request.config.getoption("--osType").
Overall, this code allows users to specify command-line options (--browser and --osType) when running pytest, and fixtures (browser and osType) allow tests to access these options during test execution. These options can be useful for configuring test environments and behavior based on the user's needs.
"""
import pytest

@pytest.fixture()
def setUp():
    print("Running conftest demo method setup")
    yield
    print("Running conftest demo method teardown")

#one fixture can call the another fixture as below
@pytest.fixture(scope="class")
def oneTimeSetup(browser,osType):
    print("Running conftest method one time setup")
    if browser=="firefox":
        print("Running test in firefox")
    else:
        print("Running test in Chrome")

    if osType=="window":
        print("Running tests in windows system")
    else:
        print("Running test in Others OS")

    yield
    print("Running conftest method one time teardown")

#extra option
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="Type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


