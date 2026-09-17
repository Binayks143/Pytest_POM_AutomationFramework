import pytest

@pytest.fixture()
def data_load():
    print("data from fixture")
    return ("data1","data2","data3")
@pytest.fixture(params=["Browser",('Chrome1','Chrome2'),"firefox"])
def parameterizetesting(request):
    return request.param

