#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

browser = webdriver.Firefox()

class SeleniumTest:
    def checkWord(self,url,word):
       
        browser.get(url)
        main = browser.execute_script("return document.documentElement.outerHTML")
        countMain = main.count(word)
        
        browser.get(url)
        servicios = browser.execute_script("return document.documentElement.outerHTML")
        serviciosCount = servicios.count(word)
        
        browser.get(url)
        clientes = browser.execute_script("return document.documentElement.outerHTML")
        clientesCount = clientes.count(word)
        
        browser.get(url)
        contactanos = browser.execute_script("return document.documentElement.outerHTML")
        contactanosCount = contactanos.count('word)
        
        browser.get(url)
        unete = browser.execute_script("return document.documentElement.outerHTML")
        uneteCount = unete.count(word)
        
        result = countMain + serviciosCount + clientesCount + contactanosCount + uneteCount
        
        browser.close()
        
        return result

SeleniumTest = SeleniumTest()
res = SeleniumTest.checkWord()
print(res)
