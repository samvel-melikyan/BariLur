
from selenium import webdriver
import main


class BaseDriver:
    """Initializing a web driver with its attributes"""


    @staticmethod
    def set_driver_none(self):
        main.driver = None

    @staticmethod
    def get_driver(self):
        if main.driver is None:
            main.driver = webdriver.Firefox()
        return main.driver

    def text(self):
        print("-BaseDriver-")





