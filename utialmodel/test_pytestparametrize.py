"""
@Time     :   2020/8/5 15:02
@Author   :   Winter
@File     :   test_pytestparametrize.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
import time
import pytest
import allure


deviceModule = [2, 3]


@pytest.mark.parametrize("data1", deviceModule)
@allure.feature("hello")
def test_data(data1):
    json_message = {
        "list": [
            {
                "accountId":    12345,
                "openId":   5678,
                "data": {
                    "deviceModule": data1
                }
            }

        ]
    }
    print(json_message)


data = [
    {
        "name": "abc",
        "iphone": "124546",
    },
    {
        "name": "def",
        "iphone": "789012"
    }
]


@pytest.mark.parametrize('data1', data)
def test_dic(data1):
    print(data1)
    print("name is ", data1["name"], "iphone is ", data1["iphone"])


if __name__ == '__main__':
    pytest.main(['-sv', 'test_pytestparametrize.py'])

