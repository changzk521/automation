from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


#添加启动配置
option = webdriver.ChromeOptions()

option.add_argument('disable-infobars')

#打开浏览器
driver = webdriver.Chrome(chrome_options=option)

driver.maximize_window()

driver.add_cookie()
driver.get("http://bjweb.tj.aqdpay.com/gxoperation/parentChildTree/rightsRules")




