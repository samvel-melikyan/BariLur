from selenium import webdriver


class BaseDriver:
    """Initializing a web driver with its attributes"""

    def __init__(self):
        self.driver = webdriver.Firefox()



