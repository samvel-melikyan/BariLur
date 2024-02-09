import time

from selenium.webdriver.common.by import By

from BariLur.pages.base_page import BasePage
import main


class Home(BasePage):
    def __init__(self):
        super().__init__()
        # self.wait = WebDriverWait(main.driver, 10)
        # self.papers = self.wait.until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div")))
        self.papers = main.driver.find_elements(By.CSS_SELECTOR, "#root > div > div.HomePage > div.CurrentJournals > div") #//*[@id='root']/div/div[2]/div[2]/div")


    def paper_list(self):
        time.sleep(5)
        return self.papers





