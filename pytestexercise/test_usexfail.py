# coding=utf-8
import pytest
import sys
'''
xfail：标记测试用例是期望失败的
在参数化中可以将skip/xfail作为一个独立的实例当作marker使用：
'''


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k"))
    ]
)
def test_increment(n, expected):
    assert n + 1 == expected
