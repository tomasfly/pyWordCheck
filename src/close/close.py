class CloseBrowser(object):

    def __init__(self,browser):
        self.browser = browser

    def close(self):
        self.browser.close()
        return True