from unittest import TestCase
from ..close.close import CloseBrowser

class TestClose(TestCase):

    def test_close_browser(self): 
        cb = CloseBrowser('Browser')