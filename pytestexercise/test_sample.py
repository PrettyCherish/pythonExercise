# coding=utf-8
# 在test_sample.py的同级目录下直接执行pytest
# pytest会运行当前目录及子目录下所有以test_*py和*_test.py命名的文件。


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
