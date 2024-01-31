import null
from selenium.webdriver.chrome import webdriver

from BariLur.util.BaseDriver import BaseDriver


class BaseTest:
    driver = webdriver
    def setUp(self):
        self.driver = BaseDriver.getDriver()

    def tearDown(self):
        if self.driver != null:
            self.driver.quit()
            self.setDriver(null)


