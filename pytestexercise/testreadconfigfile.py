# coding=utf-8
import configparser
import os
import time


class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))    # 获取项目根目录的相对路径
        print(root_dir)

        config = configparser.ConfigParser()
        file_path = root_dir + '/pythonbasic/config.ini'
        config.read(file_path)  # 用来读取配置文件config.ini

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        return browser, url

    def get_system_time(self):
        print(time.time())
        print(time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(new_time)


trcf = TestReadConfigFile()
print(trcf.get_value())
trcf.get_system_time()
