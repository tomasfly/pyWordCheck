#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()

class SeleniumTest:
    def checkWord(self):
       
        browser.get('http://www.fhios.es/')
        main = browser.execute_script("return document.documentElement.outerHTML")
        countMain = main.count('Fhios')
        
        browser.get('http://www.fhios.es/servicios')
        servicios = browser.execute_script("return document.documentElement.outerHTML")
        serviciosCount = servicios.count('Fhios')
        
        browser.get('http://www.fhios.es/clientes')
        clientes = browser.execute_script("return document.documentElement.outerHTML")
        clientesCount = clientes.count('Fhios')
        
        browser.get('http://www.fhios.es/contactanos')
        contactanos = browser.execute_script("return document.documentElement.outerHTML")
        contactanosCount = contactanos.count('Fhios')
        
        browser.get('http://www.fhios.es/unete')
        unete = browser.execute_script("return document.documentElement.outerHTML")
        uneteCount = unete.count('Fhios')
        
        result = countMain + serviciosCount + clientesCount + contactanosCount + uneteCount
        
        browser.close()
        
        return result

SeleniumTest = SeleniumTest()
res = SeleniumTest.checkWord()
print(res)