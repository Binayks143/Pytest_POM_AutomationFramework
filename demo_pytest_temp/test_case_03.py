"""
Using the conftest config file to run the fixture
to run : python -m pytest .\test_case_03.py -s -v --browser firefox
--browser firefox : command line input -
"""
import pytest

def testMethodA(oneTimeSetup,setUp):
    print("Test Method A output")

def testMethodB(oneTimeSetup,setUp):
    print("Test Method B output")