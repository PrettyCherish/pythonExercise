# coding=utf-8
import configparser
import os.path
from pythonExercise.pom_demo.framework.logger import Logger
from selenium import webdriver

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    dir = os.path.abspath(os.path.dirname(__file__))    # 获取相对路径

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\config\\config.ini'
        '''
        # 获取当前目录
        os.path.abspath(os.path.dirname(__file__))
        os.path.abspath(os.getcwd())
        # 获取上一级目录路径
        os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        os.path.abspath(os.path.dirname(os.getcwd()))
        os.path.abspath(os.path.join(os.getcwd(), ".."))
        # 获取上上级目录路径
        os.path.abspath(os.path.join(os.getcwd(), "../.."))
        '''
        print(file_path)
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
        if browser == "Chrome":
            driver = webdriver.Chrome()

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
