# By: Kenny_G_Loggins
# Created on: 8/7/20, 4:19 PM
# File: splash.py
# Project: F1_discord_bot


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent'

driver.get(URL)


def S(X):
    return driver.execute_script('return document.body.parentNode.scroll' + X)


# May need manual adjustment S('Width'), S('Height')
driver.set_window_size(500, 1000)
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()
