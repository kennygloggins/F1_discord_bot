# By: Kenny_G_Loggins
# Created on: 8/7/20, 4:19 PM
# File: splash.py
# Project: F1_discord_bot

#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = ''

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(500,1000) # May need manual adjustment S('Width'), S('Height')
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()