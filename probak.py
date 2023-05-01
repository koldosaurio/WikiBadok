# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:00:49 2023

@author: Lorea
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import funtzioak
import csv
import aldagaiGlobalak as ag

url = "https://www.badok.eus/euskal-musika/madarikatuak"
html = urlopen(url).read().decode("utf-8")
soup =  BeautifulSoup(html, 'html.parser')
datuak = funtzioak.__izenak_lortu()
datuak[0] =funtzioak.__taldearen_informazioa_lortu(datuak[0]['url'], datuak[0])
for diska in datuak[0]['diskak']:
	print(diska)
#print(funtzioak.taldearen_informazioa_lortu(url, {}))