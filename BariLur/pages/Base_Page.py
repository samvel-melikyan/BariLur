
from BariLur.util import BaseDriver
from selenium.webdriver.common.by import By
from HomePage import Home
from ArchivePage import Archive
from AboutPage import About
from LinksPage import Links
from RequestPage import Request


class BasePage(BaseDriver):
    """This class is contains the common features of every page"""

    BASE_URL = "http://barilur.org/index.html"


    def __init__(self):
        super().__init__()
        self.home = driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li.current > a")
        self.archive = driver.find_element(By.CSS_SELECTOR, "#container > div:nth-child(1) > ul > li.current > a")
        self.links = super.driver.find_element(By.CSS_SELECTOR, "#container > div:nth-child(1) > ul > li:nth-child(5) > a")
        self.request = super.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li.current > a")
        self.about = super.driver.find_element(By.CSS_SELECTOR, "#container > div > ul > li:nth-child(7) > a")
        self.driver.get(self.BASE_URL)

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
