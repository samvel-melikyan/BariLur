from selenium.webdriver.common.by import By

import main
from BariLur.pages.base_page import BasePage
from BariLur.util.custom_element_actions import MyActions


class Home(BasePage):
    def __init__(self):
        super().__init__()
        self.journal = main.driver.find_elements(By.CSS_SELECTOR, ".CurrentJournals.box.title")
        # self.journal1 = main.driver.find_element(By.CSS_SELECTOR, "div.HomePage > div.CurrentJournals > div:nth-child(1) > p")
        self.text = main.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/p[1]/b")
        self.titles = main.driver.find_elements(By.CSS_SELECTOR, "#root > div > div.HomePage > div.CurrentJournals > div > p") # (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/p/text") #
        self.journal_list = []


    def journals_list(self):
        return self.journal

    def journal_title(self):
        titles = []
        # print(titles)
        # print(self.titles)
        # for i in self.titles:
        #     titles.append(MyActions.get_text(i))
        # for i in self.journal:
        #     a = i.text
        #     print(f"#{a.encode()}")
        print(self.text.text.encode('utf-8'))
        # print(f"after loop {titles}")
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







