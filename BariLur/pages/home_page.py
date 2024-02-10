import time

from selenium.webdriver.common.by import By

from BariLur.pages.base_page import BasePage
from BariLur.util.custom_element_actions import MyActions
from BariLur.util.wait_helpers import WaitHelper
import main


class Home(BasePage):
    def __init__(self):
        super().__init__()
        self.papers = main.driver.find_elements(By.CSS_SELECTOR, "#root > div > div.HomePage > div.CurrentJournals > div") #//*[@id='root']/div/div[2]/div[2]/div")


    def paper_list(self):
        WaitHelper().until_visible((By.CSS_SELECTOR, "#root > div > div.HomePage > div.CurrentJournals > div"))
        return self.papers

    def archive(self):
        MyActions().click(self.archive)





