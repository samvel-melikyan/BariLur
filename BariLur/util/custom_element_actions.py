from BariLur.util.wait_helpers import WaitHelper
class MyActions:
    wait = WaitHelper()
    def click(self, element):
        self.wait.until_clickable(element)
        element.click()

    def send_keys(self, element, text):
        self.wait.until_visible_of(element)
        element.clear()
        element.send_keys(text)

    def get_text(self, element):
        self.wait.until_text_to_be_present()
        return element.text

    def get_attribute(self, element, attribute):
        self.wait.until_visible_of(element)
        return element.get_attribute(attribute)

    def get_location(self, element):
        """returns a dictionary of element's location"""
        self.wait.until_visible_of(element)
        return element.location

    def get_size(self, element):
        """returns a dictionary  of element's size"""
        self.wait.until_visible_of(element)
        return element.size

    def find_elements(self, location):
        return self.wait.until_presence_of_all(location)

    def find_element(self, location):
        return self.wait.until_visible_of(location)



