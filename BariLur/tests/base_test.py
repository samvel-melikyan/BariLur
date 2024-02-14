import unittest
import main


class BaseTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        from BariLur.util.base_driver import BaseDriver
        BaseDriver.get_driver(self=None)
        main.driver.get(main.BASE_URL)

    @classmethod
    def tearDown(cls):
        if main.driver is not None:
            main.driver.quit()
        from BariLur.util.base_driver import BaseDriver
        BaseDriver.set_driver_none(self=None)



