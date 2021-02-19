from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def start_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://bjweb.tj.aqdpay.com/gxoperation/login')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div/input').send_keys("admin")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div/input').send_keys("123456")
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[6]/li/div').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[6]/li/ul/div[2]/a/li').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/button').click()
    # 停留1秒,移动到该元素并点击(权益名称)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[1]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[7]').click()
    # 停留1秒,移动到该元素并点击(起始位置)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[2]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[4]').click()
    # 停留1秒,移动到该元素并点击(是否为金果子)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[3]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]/span').click()
    # 停留1秒,移动到该元素并点击(起始时间)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[4]/div/div/input[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/table/tbody/tr[4]/td[5]/div').click()
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[2]/table/tbody/tr[4]/td[7]/div').click()
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/button[2]').click()
    # 停留1秒,移动到该元素并点击(进度值)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[5]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[5]/div/div/input').send_keys("2")
    # 停留1秒,移动到该元素并点击(增长值)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[6]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[6]/div/div/input').send_keys("2")
    # 停留1秒,移动到该元素并点击(增长周期)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[7]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[7]/div/div/input').send_keys("2")
    # 停留1秒,移动到该元素并点击(提交)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[8]/div/button').click()
    # 停留1秒,移动到该元素并点击(确定)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[2]/span').click()

    # 停留1秒,移动到该元素并点击(搜索条件)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[3]/div/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[4]').click()
    # 停留10s
    time.sleep(10)
    # 关闭浏览器
    driver.close()





