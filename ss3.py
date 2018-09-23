# firs conpy FireFox driver into the scripts folder inside anaconda 

# scenario3
"""
- Open website and take screnshot
- specify the window width and height
"""

# from selenium import webdriver
# # DRIVER = 'chromedriver'
# driver = webdriver.Firefox()

# # get driver
# driver.maximize_window()
# driver.get('http://www.iherb.com')

# # set the window size
# # width = 1200
# # height = 800
# # driver.set_window_size(width, height)

# # take screenshot
# screenshot = driver.save_screenshot('output\myfirstFireFox.png')
# driver.close()


from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.iherb.com")


# scroll some more
for isec in (4, 3, 2, 1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / %s);" % isec)
    sleep(1)

# load more
sleep(2)
print("push Load more...")
# driver.find_element_by_css_selector('button.load-more-button').click()

print("wait a bit...")
sleep(2)

print("Jump to the bottom, work our way back up")
for isec in (1, 2, 3, 4, 5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / %s);" % isec)
    sleep(1)

driver.execute_script("window.scrollTo(0, 0)")
print("Pausin a bit...")
sleep(2)
print("Scrollin to the top so that the nav bar isn't funny looking")
driver.execute_script("window.scrollTo(0, 0);")


sleep(1)
print("Screenshotting...")
# screenshot
driver.save_screenshot("output\screenshot.com.png")

driver.close()