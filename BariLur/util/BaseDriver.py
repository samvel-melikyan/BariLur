
from selenium import webdriver


class BaseDriver:
    """Initializing a web driver with its attributes"""
    driver = None

    def setDriver(self, driver):
        self.driver = driver

    def getDriver(self):
        if self.driver is None:
            self.driver = webdriver.Firefox()
        return self.driver





