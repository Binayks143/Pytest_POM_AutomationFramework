import pytest

"""
it indicates the point where the setup code above the yield statement will be run before each 
test that uses the fixture, and the teardown code below the yield statement will be run after each test.
"""


@pytest.fixture()
def setUp():
    print("Once Before Every Method")
    yield
    print("Once After Every Method")

def test_methodA():
    print("this is Test Method A")

# Will run the fixture before this method
def test_methodB(setUp):
    print("This is test method B")