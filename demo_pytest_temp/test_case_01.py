import pytest

"""
File name should be strat with test
test method name should strat with test

pytest --> Run all the test cases
pytest test_module.py --> Run the particular test file
py.test test_module.py::test_method --> run the selected method under python file

-s print the statement
-v verbose 

e.g :  
To Run: 
Go to path and use python -m pytest -v -s
"""

@pytest.fixture()
def setUp():
    print("Once Before Every Method")
def test_methodA():
    print("this is Test Method A")

# Will run the fixture before this method
def test_methodB(setUp):
    print("This is test method B")
