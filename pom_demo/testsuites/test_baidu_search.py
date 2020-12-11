# coding=utf-8
import time
import unittest
from pythonExercise.pom_demo.framework.browser_engine import BrowserEngine
from pythonExercise.pom_demo.pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):

        # 1.直接调用对应的方法
        # self.driver.find_element_by_id('kw').send_keys('selenium')
        # time.sleep(1)
        # try:
        #   assert 'selenium' in self.driver.title
        #       print('Test Pass.')
        #       except Exception as e:
        #       print('Test Fail.', format(e))

        # 2.通过调用封装的方法进行调用。
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')    # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()


if __name__ == '__main__':
    unittest.main()
