# coding=utf-8
import pytest


'''
工厂化的fixture模式对于一个fixture在单一测试中需要被多次调用非常有用。fixture用一个生成数据的函数
取代了原有的直接返回数据。该函数 可以在测试中被多次调用。
如有需要，工厂可以携带参数：
'''
@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {
            "name": name,
            "order": []
        }
    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Tome")
    print(customer_1, customer_2, customer_3)


if __name__ == '__main__':
    pytest.main(["-s", "test_facfixture.py"])
