from selenium import webdriver

class InitTests(object):

    def getDriver(self,url):
        browser = webdriver.Firefox()
        browser.get(url)
        return browser
