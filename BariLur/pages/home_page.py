import time

from selenium.webdriver.common.by import By

from BariLur.pages.base_page import BasePage
from BariLur.util.custom_element_actions import MyActions
from BariLur.util.wait_helpers import WaitHelper
import main


class Home(BasePage):
    def __init__(self):
        super().__init__()
        self.papers = main.driver.find_elements(By.CLASS_NAME, "box")


    def paper_list(self):
        MyActions().find_elements((By.CLASS_NAME, "box"))
        return self.papers

    def archive(self):
        MyActions().click(self.archive)





