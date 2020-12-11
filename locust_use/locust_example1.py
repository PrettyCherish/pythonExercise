"""
@Time     :   2020/9/25 19:40
@Author   :   Winter
@File     :   locust_example1.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
import time
from locust import HttpUser,task,between
import requests


""" HttpUser是最常用的User。它添加了一个client属性，用于发出HTTP请求。
    client是HttpSession。HttpSession是requests.Session因此，它的特性已经有了很好的文档记录，
    并且应该为许多人所熟悉。HttpSession添加的主要内容是将请求结果报告到Locust(成功/失败、响应时间、
    响应长度、名称)。
"""


class InterFaceCVist(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def get_vist(self):
        req = self.client.post("https://www.baidu.com")
        print(req.status_code)


if __name__ == '__main__':
    import os
    os.system("locust -f locust_example1.py")
