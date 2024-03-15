"""
To Learn:
1. How to use test class to warp methods under one class
2. What is autouse keywords in fixture
3. Assert the result
Stub method : dummyClass_to_test_05.py
4. TO generate the HTML report use: --html=path_withFileName.html
if we don't give the path it will generate the report in project directory.
e.g.python -m pytest .\test_realExample_05.py -s -v --browser firefox --osType mac --html=report.html

"""

import pytest
from demo_pytest_temp.dummyClass_to_test_05 import stubMethod

#usefixtures use to take fisture and based on scope auto pick up will happen

@pytest.mark.usefixtures("oneTimeSetup","setUp")
class TestRealTimeExample():

#auto use : automatically run this fixture
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc=stubMethod(10)

    def test_methodA(self):
        result=self.abc.sumNumber(6,8)
        assert result==24
        print("Running Method A")

    def test_methodB(self):
        result=self.abc.sumNumber(6,8)
        assert result > 40
        print("Running Method B")



