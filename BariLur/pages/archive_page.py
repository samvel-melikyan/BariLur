from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import main
from BariLur.util.custom_element_actions import MyActions
from BariLur.pages.base_page import BasePage

class Archive(BasePage):
    def __init__(self):
        super().__init__()
        self.year = main.driver.find_element(By.CSS_SELECTOR, "#root > div > div.ArchivePage > div.ArchiveSearchBar > div > select")
        self.search_area = main.driver.find_element(By.CSS_SELECTOR, "#root > div > div.ArchivePage > div.ArchiveSearchBar > form > input[type=text]:nth-child(1)")
        self.search_button = main.driver.find_element(By.CSS_SELECTOR, "#root > div > div.ArchivePage > div.ArchiveSearchBar > form > input[type=submit]:nth-child(2)")


    def get_year_list(self):
        select = Select(self.year)
        year_list = [month for month in select.options]
        return year_list

    def get_content_header(self):
        return MyActions().get_text(main.driver.find_element(By.CLASS_NAME, "heading"))

    def get_content_headers_list(self):
        return MyActions().get_text(main.driver.find_elements(By.CLASS_NAME, "sub_content"))

