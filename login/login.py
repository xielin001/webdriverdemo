# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import sys

#实例化

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

# #设置浏览器的像素
# driver.set_window_size(1920, 1080)
# #输入用户名
# driver.find_element_by_id("username").clear()
# driver.find_element_by_id("username").send_keys("admin")
# #输入密码
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("123456")
# #输入验证码
# driver.find_element_by_id("valida").clear()
# driver.find_element_by_id("valida").send_keys("0000")
# #点击登陆
# driver.find_element_by_id("Login").click()
