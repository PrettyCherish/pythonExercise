# coding:utf-8
# 使用allure生成测试报告
# 1.pytest -v test_useallure.py --alluredir report/result/
# 2.allure generate report/result/ -o report/html --clean
# 3.allure open -h 127.0.0.1 -p 8088 ./report/html
import pytest
import time as t


def add(a, b):
    try:
        return a+b
    except Exception as e:
        return e.args[0]


@pytest.mark.parametrize('a,b,result', [
      (1,1,2),
      (1.0,1.0,2.0),
      (1, 1.0, 2.0),
      (1,0,1),
      ('','',''),
      ('hi ','wuya','hi wuya'),
      (0, '', "unsupported operand type(s) for +: 'int' and 'str'"),
      (1,'hi',"unsupported operand type(s) for +: 'int' and 'str'"),
      (1.0,'wuya',"unsupported operand type(s) for +: 'float' and 'str'"),
])
def test_add(a, b, result):
    t.sleep(1)
    assert add(a, b) == result
