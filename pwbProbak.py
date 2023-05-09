# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:19:00 2023

@author: Lorea
"""

import pwbFuntzioak as funtzioak
import pywikibot
import funtzioak as f
import csv
import csvreader as c
"""
with open('diskak.csv', mode='r') as diskak:
    diskak_reader = csv.reader(diskak)
    for row in diskak_reader:
        print(row[0], row[1])
"""

site = pywikibot.Site("test", "wikidata")
izena='Badok Proba 2'
statementCode='P94318'
targetCode='Q1785'

itemCode ='Q229612'

#funtzioak.add_statement(site, itemCode, statementCode, targetCode, 'https://example.com/')
#print(funtzioak.get_statement_codes(site, itemCode))
#funtzioak.add_dateStatement(site, itemCode, 'P94385', 2023)

#funtzioak.add_reference(site, itemCode, 'P93', 'https://es.wikipedia.org/wiki/Harry_Styles')

"""
datuak =f.__izenak_lortu()
for i in range(len(datuak)):
	if datuak[i]['izena'].lower()=='nafarroa 1512':
		datuak[i] =f.__taldearen_informazioa_lortu(datuak[i]['url'], datuak[i])
		funtzioak.taldeBerriaSortu(site,datuak[i])
"""
#print(funtzioak.csv_to_dict("taldeak.csv", "diskak.csv"))


#print(c.lortuGeneroak('Elektronikoa'))

print(c.lortuGeneroak('"Rock, Pop-rock"'))
