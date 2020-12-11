"""
@Time     :   2020/7/24 17:30
@Author   :   Winter
@File     :   test.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
# driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()

