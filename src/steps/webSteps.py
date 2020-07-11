# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class WebSteps(object):
    
    def __init__(self, browser):
        self.servicios = "//a[text()='Servicios']"
        self.clientes = "//a[text()='Clientes']"
        self.equipo = "//a[text()='Equipo']"
        self.contacto = "//a[text()='Contacto']"
        self.unete = "//a[text()='Únete']"
        self.aceptar = "//a[text()='Aceptar']"
        self.t = self.servicios,self.clientes,self.equipo,self.contacto,self.unete
        self.browser = browser        

    def goToUrl(self,url):
        self.browser.get(url)
    
    def getElementsByXpath(self,xpath):
        elements = self.browser.find_elements(By.XPATH,xpath)
        return elements
    def getCount(self,elements,word):
        total = 0
        for element in elements:
            if element.is_displayed() is True:
                if word in element.text:
                    total = total + 1
        return total
    def getCountSingleString(self,elements,word):
        text = elements[0].text
        count = text.upper().count(word.upper())
        return count            
    def getElementByText(self,text):
        self.browser.find_element_by_xpath(text)
    def checkWordTest(self,word):
        total = 0
        aceptar = self.browser.find_element(By.XPATH, self.aceptar)
        aceptar.click()
        for xpath in self.t:
            element = self.browser.find_element(By.XPATH,xpath)
            element.click()
            # allElements = self.getElementsByXpath('//*')
            allElements = self.getElementsByXpath('//body')
            totalPage = self.getCountSingleString(allElements,'Fhios')
            total = total + totalPage            
        return total
         