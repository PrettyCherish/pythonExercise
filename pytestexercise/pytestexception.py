# coding=utf-8
import pytest


# 使用pytest.raises可以捕获异常，可以用excinfo来显示异常的详细信息；
# excinfo是ExceptionInfo的一个实例。主要属性是.type,.value,.traceback
# 使用pytest.raises更适合测试自己的代码故意引发的异常。
def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        print(1 / 0)
    assert 'division by zero' in str(excinfo.value)


if __name__ == '__main__':
    test_zero_division()
