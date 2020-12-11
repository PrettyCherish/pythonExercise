"""
@Time     :   2020/8/21 16:20
@Author   :   Winter
@File     :   use_swipe.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
import os
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


# appium 服务监听地址
server = 'http://localhost:4723/wd/hub'
# app启动参数
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI"
}


# 驱动
driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 30)
# 获取登录按钮




