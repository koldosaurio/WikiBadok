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
funtzioak.diskaren_datuak_lortu(soup)
