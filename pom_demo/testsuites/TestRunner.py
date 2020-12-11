# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time


# 设置报告文件保存路径
report_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/test_report/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

# 设置报告名称格式
htmlfile = report_path + now + "HTMLtemplate.html"

fp = open(htmlfile, "wb")

# 构建suite;discover用于加载指定目录下所有测试用例。
suite = unittest.TestLoader().discover('../testsuites')


if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用于生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"pom项目测试报告", description=u'用例测试情况')
    # 执行测试计划
    runner.run(suite)
