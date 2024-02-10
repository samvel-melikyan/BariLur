from BariLur.util.wait_helpers import WaitHelper
class MyActions:
    wait = WaitHelper()
    def click(self, element):
        self.wait.until_clickable(element)
        element.click()




