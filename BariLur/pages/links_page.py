import main
from BariLur.util.custom_element_actions import MyActions
from BariLur.pages.base_page import BasePage

class Links(BasePage):
    def __init__(self):
        super().__init__()
        self.Bible_in_armenian = MyActions().find_element("#root > div > div.LinksPage > a")
        self.eng_version = MyActions().find_element("#root > div > div.LinksPage > p > a")

    def Bible_in_armenian(self):
        MyActions().click(MyActions().find_element("#root > div > div.LinksPage > a"))
        # return

    def eng_version(self):
        MyActions().click(MyActions().find_element("#root > div > div.LinksPage > p > a"))
