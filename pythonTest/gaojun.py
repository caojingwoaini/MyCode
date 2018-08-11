# --*-- coding:utf-8 --*--

from selenium import webdriver
import time

br=webdriver.Chrome()
br.get("https://www.baidu.com")
time.sleep(8)
br.quit()


