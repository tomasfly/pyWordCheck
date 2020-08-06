#!/usr/bin/env python
from src.steps.webSteps import WebSteps
from src.init.initTests import InitTests
from src.close.close import CloseBrowser

targetUrl = 'http://www.example.com/'

it = InitTests()
browser = it.getDriver(targetUrl)
ws = WebSteps(browser)
words = ws.checkWordTest('Test')
print(words)
close = CloseBrowser(browser)
close.close()
