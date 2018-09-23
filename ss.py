# firs conpy webdriver.exe into the scripts folder inside anaconda 

#scenario1
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('http://www.iherb.com')

#scenario2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

# command opens a website
browser.get('http://www.iherb.com')
# asserherb' in browser.title

#command searches for element p 
elem = browser.find_element_by_name('kw') # find the search box
#command enters keyword and searches for word
elem.send_keys('SIX-06459'+ Keys.RETURN)


# browser.quit()