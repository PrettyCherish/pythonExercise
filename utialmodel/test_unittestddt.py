"""
@Time     :   2020/7/17 15:06
@Author   :   Winter
@File     :   test_unittestddt.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
import unittest
import os
from ddt import ddt, data, unpack, file_data


@ddt
class Testwork(unittest.TestCase):

    # 1.单组元素
    @data(1, 2, 3)
    def test_01(self, value):
        print(value)

    # 2.多组未分解元素
    @data((1, 2, 3), (4, 5, 6))
    def test_02(self, value):
        print(value)

    # 3.多组分解元素
    @data((1, 2, 3), (4, 5, 6))
    @unpack     # 拆分数据
    def test_03(self, value1, value2, value3):   # 每组数据有3个
        print(value1, value2, value3)


if __name__ == '__main__':

    unittest.main()
