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
import csvreader as rd

url = "https://www.badok.eus/euskal-musika/a-maiah"
html = urlopen(url).read().decode("utf-8")
soup =  BeautifulSoup(html, 'html.parser')

print(rd.lortu_datuak('taldeak.csv', 'diskak.csv', ''))
# rd.lortu_datuak('taldeak.csv', 'diskak.csv', '')

# datuak = funtzioak.__izenak_lortu()


# file= open('probak.csv', 'w', newline='')
# writer = csv.writer(file)


# datuak[0] = funtzioak.__taldearen_informazioa_lortu(datuak[0]['url'], datuak[0])
# print(datuak[0])
# writer.writerow([datuak[0]['id'], datuak[0]['izena'],datuak[0]['biografia'], datuak[0]['urtea'], datuak[0]['herria'], datuak[0]['generoak'], datuak[0]['url']])

# file.close()