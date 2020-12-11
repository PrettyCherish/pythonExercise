"""
@Time     :   2020/7/17 11:49
@Author   :   Winter
@File     :   test_parametrize.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
@Details  :   pytest进行数据驱动测试。即数据参数化
"""
# coding=utf-8
import pytest


data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]


def add(a, b):
    return a + b

# 当装饰器装饰测试类时，给数据集合会被传递给给类的所有方法
@pytest.mark.parametrize('a, b, expect', data_1)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数2测试数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect


data = [
    [1, 2, 3],
    [4, 5, 9]
]   # 列表嵌套列表
data_tuple = [
    (1, 2, 3),
    (4, 5, 9)
]   # 列表嵌套元组

# 当装饰器测试函数如下：
@pytest.mark.parametrize('a, b, expect', data)
def test_parametrize_3(a, b, expect):   # 一个参数接收一个数据
    print('\n测试数据为\n{},{},{}'.format(a, b, expect))
    assert a + b == expect


@pytest.mark.parametrize('value', data)
def test_parametrize_4(value):  # 一个参数接收一组数据
    print('\n测试数据为\n{}'.format(value))
    assert value[0] + value[1] == value[2]


# 组合数据
data_2 = [1, 2]
data_3 = [3, 4]
@pytest.mark.parametrize('a', data_2)
@pytest.mark.parametrize('b', data_3)
def test_parametrize_5(a, b):
    print('\n测试数据为\n{},{}'.format(a, b))


if __name__ == '__main__':
    pytest.main(['-sv', 'test_parametrize.py'])
