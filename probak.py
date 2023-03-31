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

url = "https://www.badok.eus/euskal-musika/a-tuti-plain/a-tuti-plain"
html = urlopen(url).read().decode("utf-8")
soup =  BeautifulSoup(html, 'html.parser')
#print(funtzioak.taldearen_informazioa_lortu(url, {}))
#print(funtzioak.diskaren_datuak_lortu(soup))

datuak=funtzioak.datuak_lortu()
with open('taldeak.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for i in range(len(datuak)):
		if datuak[i]['izena'] in ag.IZEN_FILTROA:
			for diska in datuak[i]['diskak']:
				writer.writerow([datuak[i]['izena'], diska['izena'], datuak[i]['url']])