# coding=utf-8
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.qq.com')
sleep(3)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="top-login"]/div[3]/a').click()
# 进入iframe
driver.switch_to.frame('ptlogin_iframe')
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()

# 进入iframe
# driver.switch_to.frame('ptlogin_iframe')
driver.find_element_by_xpath('//*[@id="u"]').send_keys('871532887')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('ly871532887')
driver.find_element_by_xpath('//*[@id="login_button"]').click()

sleep(3)
driver.quit()

