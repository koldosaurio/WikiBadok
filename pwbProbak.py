# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:19:00 2023

@author: Lorea
"""

import pwbFuntzioak as funtzioak
import pywikibot
import funtzioak as f

site = pywikibot.Site("wikidata", "wikidata")
izena='Badok Proba 2'
statementCode='P94318'
targetCode='Q1785'

itemCode ='Q229997'

#funtzioak.add_statement(site, itemCode, statementCode, targetCode)

#funtzioak.add_dateStatement(site, itemCode, 'P94385', 2023)

#funtzioak.add_reference(site, itemCode, 'P93', 'https://es.wikipedia.org/wiki/Harry_Styles')


datuak =f.__izenak_lortu()
for i in range(len(datuak)):
	if datuak[i]['izena'].lower()=='nafarroa 1512':
		datuak[i] =f.__taldearen_informazioa_lortu(datuak[i]['url'], datuak[i])
		funtzioak.taldeBerriaSortu(datuak[i])
