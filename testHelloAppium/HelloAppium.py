from appium import webdriver
import time


def set_up():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    # 平台
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '5.1'
    # 设备名称
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 包名称
    desired_caps['appPackage'] = 'com.android.settings'
    # 应用程序
    desired_caps['appActivity'] = '.Settings'
    # unicode键盘
    desired_caps['unicode keyboard'] = True
    # 重置键盘
    desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

