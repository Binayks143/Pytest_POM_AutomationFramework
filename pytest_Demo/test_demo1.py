import pytest


def test_firsttest():
    print("hello")

@pytest.mark.xfail()
def test_firsttest1():
    a=8
    assert a==9, "test failed "
@pytest.fixture()
def setup():
    print("Doing SetUp")
    yield
    print("Doing TearDown")

def test_firsttest3(setup):
    print("doing test")





