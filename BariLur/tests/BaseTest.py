import unittest

from selenium.webdriver.chrome import webdriver

from BariLur.util.BaseDriver import BaseDriver


class BaseTest(unittest.TestCase):
    BASE_URL = "www.google.com"

    @classmethod
    def setUp(cls,):
        cls.driver = BaseDriver.getDriver()
        cls.driver.get(cls.BASE_URL)


    @classmethod
    def tearDown(cls):
        if cls.driver != None:
            cls.driver
            cls.setDriver(None)


    def test_1(self):
        if 1 == 0:
            print(False)
        print(True)



