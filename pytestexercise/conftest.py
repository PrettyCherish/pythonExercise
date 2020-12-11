# coding=utf-8
import smtplib
import pytest


'''
处理teardown的代码方式时可以使用addfinalizer函数来注册一个teardown的处理函数。如下：
'''
# @pytest.fixture(scope="module")
# def smtp_connection(request):
#     smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#
#     def fin():
#         print("teardown smtp_connection")
#         smtp_connection.close()
#     request.addfinalizer(fin)
#     return smtp_connection
'''
yield和addfinalizer在测试结束之后的调用是基本类似的，addfinalizer主要有两点不同于yield：
1.可以注册多个完成函数
2.无论fixture的代码是否存在异常，addfinalizer注册的函数都会被调用，
这样即使出现了异常，也可以正常的关闭那些在fixture中创建的资源。
'''