from BariLur.pages.base_page import BasePage
from BariLur.pages.home_page import Home
from BariLur.tests.base_test import BaseTest
from BariLur.util.custom_element_actions import MyActions
import main
import time


class UnitTest(BaseTest):
    def test_1(self):
        print("+does main.driver None?: test n1")
        if main.driver is None:
            print(True)
        else:
            print(False)
            print("Working...")

    def test_2(self):
        """ instances are accessible from test method"""
        print("+accessing to method and element: test n2")
        self.base = BasePage()
        time.sleep(5)
        text = self.base.home_text.text
        if text is None:
            print("Doesn't work")
        else:
            print("Working...")
        # print(self.base.text())   # unicode error: did not understood armenian letters  #solution: encoded_text = text.encode('utf-8')

    def test_3(self):
        print("+accessing to method and element through inheritance: test n3")
        self.home = Home()
        print(self.home.home_text.text)

    def test_4(self):
        print("+checking list existence: test n4")
        self.home = Home()
        length = len(self.home.paper_list())
        if length == 3:
            print(True)
        else:
            print(False)
        print(length)

    def test_5(self):
        self.home = Home()
        MyActions().click(self.home.archive)
