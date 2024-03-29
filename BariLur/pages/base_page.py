import main
from selenium.webdriver.common.by import By

from BariLur.util.custom_element_actions import MyActions


# from BariLur.pages.HomePage import Home
# from BariLur.pages.ArchivePage import Archive
# from BariLur.pages.AboutPage import About
# from BariLur.pages.LinksPage import Links
# from BariLur.pages.RequestPage import Request
#

class BasePage:
    def __init__(self):


        # self.home = main.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li.current > a")
        self.archive = main.driver.find_element(By.CSS_SELECTOR, "#root > div > div.Header > nav > a:nth-child(2)")
        # self.links = main.driver.find_element(By.CSS_SELECTOR, "#container > div:nth-child(1) > ul > li:nth-child(5) > a")
        # self.request = main.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li.current > a")
        # self.about = main.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li:nth-child(7) > a")
        self.home_text = main.driver.find_element(By.CLASS_NAME, 'content')
        # self.titles = main.driver.find_elements(By.CSS_SELECTOR, "#root > div > div.Header > nav > a")


    def text(self):
        print("-BasePage-")
        return self.home_text.text




    # def home(self):
    #     self.home.click()
    #     return Home()
    def archive(self):
        MyActions().click(self.archive)
    # def archive(self):
    #     self.archive.click()
    #     return Archive()
    #
    # def links(self):
    #     self.links.click()
    #     return Links()
    #
    # def request(self):
    #     self.request.click()
    #     return Request()
    #
    # def about(self):
    #     self.about.click()
    #     return About()
