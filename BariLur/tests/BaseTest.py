import unittest

from selenium import webdriver

from BariLur.util.BaseDriver import BaseDriver


class BaseTest(unittest.TestCase, BaseDriver):
    BASE_URL = "https://barilur.org/"
    driver = webdriver
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()



    @classmethod
    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()



    def test_1(self):
        self.driver.get(self.BASE_URL)
        if 1 == 1:
            print(True)
        else:
            print(False)




