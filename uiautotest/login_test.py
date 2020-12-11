"""
@Time     :   2020/9/11 10:51
@Author   :   Winter
@File     :   login_test.py.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# 打开F12
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get('https://egis-cssp-dmzstg1.pingan.com.cn/m/insurance_release/index-wechat.html?channelType=0995&'
           'msspShareId=5F73D185199F4E6FB882C670530289E4&ran=0.82006009574662#/insurance/life/validate')
wait = WebDriverWait(driver, 15)

# 输入用户名hdd
driver.find_element_by_xpath('//*[@id="hfl-page"]/section/div[1]/div[2]/div/div/input').send_keys("hdd")

sleep(3)
# 点击"身份证"
driver.find_element_by_xpath('//*[@id="hfl-page"]/section/div[2]/div[2]/div/div').click()
sleep(3)

div = driver.find_element_by_xpath('//*[contains(@class,"scroller-item")][2]')
#
print(div)
js = "arguments[0].scrollIntoView();"
driver.execute_script(js, div)

# ActionChains(driver).move_to_element(div).perform()

# driver.execute_script('window.scrollBy(0,34)')

driver.find_element_by_css_selector('span[class="right-part color-high"]').click()

driver.find_element_by_xpath('//*[@id="hfl-page"]/section/div[3]/div[2]/div/div/input').send_keys("123456")

