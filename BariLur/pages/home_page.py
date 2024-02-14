from selenium.webdriver.common.by import By

import main
from BariLur.pages.base_page import BasePage
from BariLur.util.custom_element_actions import MyActions


class Home(BasePage):
    def __init__(self):
        super().__init__()
        self.journal = main.driver.find_elements(By.CLASS_NAME, "box")
        self.titles = main.driver.find_elements(By.CLASS_NAME, "title")
        self.journal_list = []


    def journals_list(self):
        return self.journal

    def journal_title(self):
        titles = []
        print(titles)
        print(self.titles)
        for i in self.titles:
            titles.append(MyActions.get_text(i))
        print(f"after loop {titles}")
        return self.titles

    def journals(self):
        for i in self.journal:
            num = 0
            self.journal_list.append({
                "title": self.titles[num],
                "journal": i
            })
            num += 1
        return self.journal_list







