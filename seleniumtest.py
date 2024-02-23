from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://www.dongchedi.com/article/7331629753662915123'
#构建对象
div = webdriver.Chrome()
#打开浏览器链接
div.get(url)
#获取元素所在位置（xpath方式）
name = div.find_elements(By.XPATH,'//*[@id="article"]/p')#登录账号
for x in name:
    print(x.text)

