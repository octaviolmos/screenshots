# firs conpy webdriver.exe into the scripts folder inside anaconda 

# scenario3
"""
- Open website and take screnshot
"""

from selenium import webdriver
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)

# get driver
driver.get('http://www.iherb.com')

# take screenshot
screenshot = driver.save_screenshot('output\myfirst.png')
driver.close()