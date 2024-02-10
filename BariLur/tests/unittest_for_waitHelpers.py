import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import main


class TestWaitHelper(unittest.TestCase):
    def setUp(self):
        self.driver = main.driver
        self.driver.get("C:\Users\User\PycharmProjects\Bari Lur\BariLur\tests\unittest_file.html")  # Replace 'path_to_test_page' with the actual path

    def test_until_title_is(self):
        WebDriverWait(self.driver, 10).until(EC.title_is("Test Page"))

    def test_until_title_contains(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Test"))

    def test_until_clickable(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "clickableButton")))

    def test_until_presence_of_element_located(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "inputField")))

    def test_until_visibility_of_element_located(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "inputField")))

    def test_until_visible_of(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "inputField")))

    def test_until_frame_to_be_available_and_switch_to_it(self):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "testFrame")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
