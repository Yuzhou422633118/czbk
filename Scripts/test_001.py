
import allure

class Test_001:

    @allure.step(title="我是test_001-1测试步骤名称")
    def test_001_1(self):
        print("---->test_001-1")
        assert True
    @allure.step(title='我是test_001-2测试步骤名称')
    def test_001_2(self):
        print("---->test_001-2")
        assert True
    @allure.step(title='我是test_001-3测试步骤名称')
    def test_001_3(self):
        print("---->test_001-3")
        assert False

