# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from selenium import webdriver
from time import sleep
from numpy import random
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains





def scraping():
        #funcion que recibe la categoria de waltmare
        #devuelve los productos en una lista llamada "d"
        driver = webdriver.Chrome('C:/Users/Tomas/Documents/GitHub/Waltmart_scrapper/chromedriver.exe')
       

        #obtiene el link (el path fue defindio al principio, y la categoria es la entrada de la funcion)
        driver.get("https://www.imperiumao.com.ar/es/eventdata.php?i=12&n=Experiencia%20x2")
        #los try y except estan para evitar que se rompan el programa si falta algun dato
        try:
            estado1 = driver.find_element_by_xpath('//table[@width="90%"]/tbody/tr[6]/td[2]/p').text
            estado2 = driver.find_element_by_xpath('//table[@width="90%"]/tbody/tr[7]/td[2]/p').text
            estado3 = driver.find_element_by_xpath('//table[@width="90%"]/tbody/tr[8]/td[2]/p').text
            print(estado1)
            print(estado2)
            print(estado3)
            if estado1 != estado2 or estado2 != estado3 or estado1 != estado3:
                print("NOTIFICACION DE ACTIVO ENVIAR WPP")
        except:
            print("ENVIAR NOTIFICCION DE FALLO")
        
        sleep(1500)
        

while True:
    scraping()    