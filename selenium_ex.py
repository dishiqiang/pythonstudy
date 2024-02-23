from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://passport.17k.com/login/'
#构建对象
div = webdriver.Chrome()
#打开浏览器链接
div.get(url)
#获取元素所在位置（xpath方式）
name = div.find_element(By.XPATH,'/html/body/form/dl/dd[2]/input')#登录账号
password = div.find_element(By.XPATH,'/html/body/form/dl/dd[3]/input')#登录密码
read = div.find_element(By.XPATH,'//*[@id="protocol"]')#用户协议同意框
login = div.find_element(By.XPATH,'/html/body/form/dl/dd[5]/input')#登录按钮
#填入表单及点击登录
name.send_keys('123456')#填入账号
time.sleep(3)
password.send_keys('125789')#填入密码
time.sleep(3)
read.click()#点击同意框
time.sleep(3)
login.click()#点击登录
time.sleep(10)
