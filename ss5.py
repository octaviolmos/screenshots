"""
This script uses a simplified version of the one here:
https://snipt.net/restrada/python-selenium-workaround-for-full-page-screenshot-using-chromedriver-2x/

It contains the *crucial* correction added in the comments by Jason Coutu.
"""

import sys

from selenium import webdriver
import unittest

# import util
from .util import partTypeNum

class Test(unittest.TestCase):
    """ Demonstration: Get Chrome to generate fullscreen screenshot """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        ''' Generate document-height screenshot '''
        url = "http://effbot.org/imagingbook/introduction.htm"
        self.driver.get(url)
        util.fullpage_screenshot(self.driver, "test.png")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])