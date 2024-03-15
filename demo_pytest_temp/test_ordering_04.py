import pytest

# to run the test case in order intsall  pip install pytest-ordering
# User @pytest.mark.run(order=3)
#https://pytest-ordering.readthedocs.io/en/develop/

@pytest.mark.run(order=3)
def test_run_order_A():
    print("Running test Order A")


@pytest.mark.run(order=1)
def test_run_order_B():
    print("Running test Order B")


@pytest.mark.run(order=4)
def test_run_order_C():
    print("Running test Order C")

@pytest.mark.run(order=2)
def test_run_order_D():
    print("Running test Order D")
