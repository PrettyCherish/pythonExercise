# 使用raise可以判断代码是否抛出了异常
# 使用"quiet"模式来执行这个测试：pytest -q test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
