# coding=utf-8
import pytest

'''
运行pytest的时候带–collect-only可以显示这些生成的IDs。
数字，字符串，布尔和None类型在测试ID中会保留他们自己的字符串的表示方式，
其他的数据对象，pytest会创建一个基于参数名的字符串。可以通过ids关键字来自定义一个字符串来表示测试ID：
'''
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    print(request.param)
    return request.param


def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "egg"
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    print(request.param)
    return request.param


def test_b(b):
    pass


if __name__ == '__main__':
    pytest.main(["-s", "ids.py"])
