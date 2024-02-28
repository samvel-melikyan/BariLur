from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import main


class WaitHelper:
    time = 15

    def until_title_is(self, element):
        """waits until the title of the current page equals the specified title"""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.title_is(element))

    def until_title_contains(self, element):
        """waits until the title of the current page contains the specified substring."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.title_contains(element))

    def until_clickable(self, element):
        """the element is visible and clickable"""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.element_to_be_clickable(element))

    def until_presence_of_element_located(self, location):
        """ waits until all elements matching the locator are present in the DOM."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.presence_of_element_located(location))

    def until_visibility_of_element_located(self, location):
        """ waits until an element is present in the DOM and visible on the page."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.visibility_of_element_located(location))

    def until_visible_of(self, element):
        """wait for the visibility of a single element."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.visibility_of(element))
    def until_presence_of_all(self, location):
        """waits until all elements matching the locator are present in the DOM."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.presence_of_all_elements_located(location))

    def until_text_to_be_present(self, element, text):
        """waits until the specified text is present within the element."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.text_to_be_present_in_element(element, text))

    def until_text_to_be_present_in_element_value(self, element):
        """waits until the specified text is present within the value attribute of the element."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.text_to_be_present_in_element_value(element))

    def until_frame_to_be_available_and_switch_to_it(self, location):
        """waits until the specified text is present within the value attribute of the element."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.frame_to_be_available_and_switch_to_it(location))

    def until_invisibility(self, location):
        """waits until the element is not present in the DOM or not visible on the page."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.invisibility_of_element_located(location))

    def until_staleness_of(self, element):
        """waits until an element is no longer attached to the DOM."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.staleness_of(element))

    def until_be_selected(self, element):
        """waits until the element is selected."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.element_to_be_selected(element))

    def until_element_located_to_be_selected(self, location):
        """waits until an element matching the locator is selected."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.element_located_to_be_selected(location))

    def until_element_selection_state_to_be(self, element):
        """waits until a specified element's selection state becomes the desired value"""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.element_selection_state_to_be(element))

    def until_located_selection_state_to_be(self, location):
        """waits until an element matching the locator has the specified selection state."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.element_located_selection_state_to_be(location))

    def until_alert_is_present(self):
        """waits until an alert is present on the page."""
        wait = WebDriverWait(main.driver, self.time)
        wait.until(EC.alert_is_present())


