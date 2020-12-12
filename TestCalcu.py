import pytest
import yaml

from Calcutor import calcu


class Testcal:

    def setup_class(self):
        print("计算开始")
        self.cal = calcu()

    def teardown_class(self):
        print("计算结束")

    # 加法测试用例
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./testdata.yml"))["jia"])
    def test_jia(self,a,b,expect):
        assert expect == round(self.cal.jia(a,b),2)

    # 减法测试用例
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./testdata.yml"))["jian"])
    def test_jian(self,a,b,expect):
        assert expect == round(self.cal.jian(a,b),2)

    # 乘法测试用例
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./testdata.yml"))["cheng"])
    def test_cheng(self,a,b,expect):
        assert expect == round(self.cal.cheng(a,b),2)

    # 除法测试用例
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("./testdata.yml"))["chu"])
    def test_chu(self,a,b,expect):
        assert expect == round(self.cal.chu(a,b),2)

    # 除数为0的情况
    @pytest.mark.parametrize("a,b", yaml.safe_load(open("./testdata.yml"))["zero"])
    def test_zero(self,a,b):
        with pytest.raises(ZeroDivisionError):
            self.cal.chu(a,b)

