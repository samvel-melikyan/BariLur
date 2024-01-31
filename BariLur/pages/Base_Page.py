
from BariLur.util import BaseDriver
from selenium.webdriver.common.by import By
from HomePage import Home
from ArchivePage import Archive
from AboutPage import About
from LinksPage import Links
from RequestPage import Request


class BasePage(BaseDriver):
    """This class is contains the common features of every page"""

    BASE_URL = "barilur.org/test"


    def __init__(self):
        super().__init__()
        self.home = self.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li.current > a")
        self.archive = self.driver.find_element(By.CSS_SELECTOR, "#container > div:nth-child(1) > ul > li.current > a")
        self.links = self.driver.find_element(By.CSS_SELECTOR, "#container > div:nth-child(1) > ul > li:nth-child(5) > a")
        self.request = self.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li.current > a")
        self.about = self.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li:nth-child(7) > a")

    def home(self):
        self.home.click()
        return Home()

    def archive(self):
        self.archive.click()
        return Archive()

    def links(self):
        self.links.click()
        return Links()

    def request(self):
        self.request.click()
        return Request()

    def about(self):
        self.about.click()
        return About()


