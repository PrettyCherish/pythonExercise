"""
@Time     :   2020/8/12 15:38
@Author   :   Winter
@File     :   test_usecacheofpytest.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
import pytest
import time


# @pytest.mark.parametrize("i", range(50))
# def test_num(i):
#     if i in(17, 25):
#         pytest.fail("bad luck")


def expensive_computation():
    print("running expensive computation...")


@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        expensive_computation()
        val = 42
        request.config.cache.set("example/value", val)
    return val


def test_function(mydata):
    assert mydata == 23
