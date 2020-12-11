"""
@Time     :   2020/8/13 14:42
@Author   :   Winter
@File     :   test_usefunction.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
from pytest import approx
import numpy as np


# pytest.approx 判断两个数字或两组数字是否在误差允许范围内相等
# approx(expected, rel=None, abs=None, nan_ok=False)

# python中浮点值运算存在误差,运行结果False
print(0.1 + 0.2 == 0.3)
# approx类使用可以进行浮点数比较
print(0.1 + 0.2 == approx(0.3))
# 同样可以用于数据集
print((0.1 + 0.2, 0.2 + 0.4) == approx((0.3, 0.6)))
# 也可以用于字典
print({'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6}))
# numpy格式的数组
print(np.array([0.1, 0.2]) + np.array([0.2, 0.4]) == approx(np.array([0.3, 0.6])))

# 可以通过参数来设置approx的相对或者绝对误差
print(1.0001 == approx(1))
print(1.0001 == approx(1, rel=1e-3))
print(1.0001 == approx(1, abs=1e-3))

# 如果指定了abs，那么比较时不会考虑相对误差，换句话说，即使误差在默认的相对误差1e-6的范围内，
# 如果超过了abs定义的误差，这两个数的比较结果也是不想等的。但是如果abs和rel都定义了，那么只
# 要满足其中任何一个，都会被认为时相等的
print(1 + 1e-8 == approx(1, abs=1e-12))
print(1 + 1e-8 == approx(1, rel=1e-6, abs=1e-12))
