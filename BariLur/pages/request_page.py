from selenium.webdriver.common.by import By

from BariLur.pages.base_page import BasePage
from BariLur.util.custom_element_actions import MyActions


class Request(BasePage):
    def __init__(self):
        super().__init__()


    def name(self, name, last_name):
        MyActions().send_keys(
            MyActions.find_element(By.NAME, "fullname"),
            name + last_name
        )

    def email(self, email):
        MyActions().send_keys(
            MyActions.find_element(By.NAME, "email"),
            email
        )

    def message(self, message):
        MyActions().send_keys(
            MyActions.find_element(By.NAME, "comments"),
            message
        )

    def submit(self):
        MyActions().click(MyActions.find_element(By.NAME, "submit"))