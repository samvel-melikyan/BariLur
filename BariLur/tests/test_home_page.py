from BariLur.pages.home_page import Home
from BariLur.tests.base_test import BaseTest


class TestHome(BaseTest):

    def test_journals_amount(self):
        home = Home()
        length = len(home.journals_list())
        print(length)
        assert length == 3

    def test_journals_representation(self):
        home = Home()
        # print(len(home.journals()))
        home.journal_title()
        # print(f"jurnal_title - {len(home.journal_title())} ")  #{len(home.journal_title())}
        # print(home.journals()[0]["title"])


