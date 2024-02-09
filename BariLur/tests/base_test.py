import time
import unittest
import main

from BariLur.pages.home_page import Home
from BariLur.pages.base_page import BasePage


class BaseTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        from BariLur.util.base_driver import BaseDriver
        BaseDriver.get_driver(self=None)
        main.driver.get(main.BASE_URL)



    @classmethod
    def tearDown(cls):
        if main.driver is not None:
            main.driver.quit()
        from BariLur.util.base_driver import BaseDriver
        BaseDriver.set_driver_none(self=None)


    def test_1(self):
        print("+does main.driver None?: test n1")
        if main.driver is None:
            print(True)
        else:
            print(False)

    def test_2(self):
        """ instances are accessible from test method"""
        print("+accessing to method and element: test n2")
        self.base = BasePage()
        time.sleep(5)
        print(self.base.home_text.text)
        print(self.base.text())

    def test_3(self):
        print("+accessing to method and element through inheritance: test n3")
        self.home = Home()
        print(self.home.home_text.text)

    def test_4(self):
        print("+checking list existence: test n4")
        self.home = Home()
        if self.home.paper_list() == 3:
            print(True)
        else:
            print(False)
        print(len(self.home.paper_list()))

