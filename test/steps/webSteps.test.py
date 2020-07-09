from src.steps.webSteps import WebSteps
from unittest import TestCase

class TestWebSteps(TestCase):
    def test_name(self):
        ws = WebSteps()
        res = ws.checkWordTest('Fhios')
        self.assertEqual(res, True)