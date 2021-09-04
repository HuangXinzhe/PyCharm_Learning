from unittest import TestCase

# 对于要进行单元测试的方法需要提前导入
from demo_02 import my_sum


class Test(TestCase):
    # 初始化方法
    def setUp(self) -> None:
        self.a = 1
        self.b = 2
        print('start')

    # 销毁
    def tearDown(self) -> None:
        print('end')

    def test_my_sum(self):
        # 测试方法正确与否
        # self.fail()
        self.assertEqual(my_sum(self.a, self.b), 3)
        # self.assertEqual(my_sum(self.a, self.b), 5)
