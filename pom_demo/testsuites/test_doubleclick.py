# coding=utf-8
from pythonExercise.pom_demo.framework.basepage import BasePage
from pythonExercise.pom_demo.framework.browser_engine import BrowserEngine
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
locate = driver.find_element_by_id('su')
actionchains = ActionChains(driver)
actionchains.double_click(locate).perform()
print("success!")
time.sleep(3)




