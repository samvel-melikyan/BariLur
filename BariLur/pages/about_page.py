from selenium.webdriver.common.by import By

from BariLur.pages.base_page import BasePage
from BariLur.util.custom_element_actions import MyActions


class About(BasePage):
    def __init__(self):
        super().__init__()


    def title(self):
        return MyActions().get_text(MyActions().find_element(By.CSS_SELECTOR, "#root > div > div.AboutPage > div > h1"))

