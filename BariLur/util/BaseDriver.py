import null as null
from selenium import webdriver


class BaseDriver:
    """Initializing a web driver with its attributes"""
    driver = null

    def setDriver(self, driver=webdriver):
        self.driver = driver

    def getDriver(self):
        if self.driver == null:
            self.driver = webdriver.Firefox()
        return self.driver





