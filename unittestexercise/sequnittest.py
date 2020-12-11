# coding=utf-8
import unittest
'''
unittest框架默认根据ACSII码的顺序加载测试用例，数字与字母的顺序为：0~9，A~Z，a~z

'''


class Test1(unittest.TestCase):
    def setUp(self):
        print("执行class Test1的setUp")

    def test_c(self):
        print("执行test_c...")

    def test_b(self):
        print("执行test_b...")

    def tearDown(self):
        print("执行class Test1的tearDown")


class Test2(unittest.TestCase):
    def setUp(self):
        print("执行class Test2的setup")

    def test_d(self):
        print("执行test_d...")

    def test_a(self):
        print("执行test_a...")

    def tearDown(self):
        print("执行class Test2的teardown")


if __name__ == '__main__':
    # 启动单元测试
    # unittest.main()

    # 获取TestSuite的实例对象
    suite = unittest.TestSuite()

    # 将测试用例添加到测试容器中
    suite.addTest(Test1('test_c'))
    suite.addTest(Test1('test_b'))
    suite.addTest(Test2('test_d'))
    suite.addTest(Test2('test_a'))

    # 创建TextTestRunner类的实例对象
    runner = unittest.TextTestRunner()
    runner.run(suite)
