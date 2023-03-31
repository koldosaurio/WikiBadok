# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:00:49 2023

@author: Lorea
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import funtzioak

url = "https://www.badok.eus/euskal-musika/a-maiah/lokarriak"
html = urlopen(url).read().decode("utf-8")
soup =  BeautifulSoup(html, 'html.parser')
#print(funtzioak.taldearen_informazioa_lortu(url, {}))

