import pytest
@pytest.mark.usefixtures()
class Test_demo1:
    def testdat1(self,data_load):
        print(data_load[1])

    def testdata2(self,parameterizetesting):
        print(parameterizetesting)
