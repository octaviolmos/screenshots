# firs conpy webdriver.exe into the scripts folder inside anaconda 

# scenario3
"""
- Open website and take screnshot
- specify the window width and height
"""

from selenium import webdriver
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)

# get driver
driver.get('http://www.iherb.com')

# set the window size
width = 1200
height = 800
driver.set_window_size(width, height)

# take screenshot
screenshot = driver.save_screenshot('output\myfirst.png')
driver.close()