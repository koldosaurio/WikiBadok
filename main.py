# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:49:06 2023

@author: Lorea
"""

import pwbFuntzioak as funtzioak
import pywikibot as pwb
import json_to_dict as json
import csvreader as csv
import aldagaiGlobalak as ag
from datetime import datetime as dt


site = pwb.Site("wikidata", "wikidata")
taldeak = csv.lortu_datuak()

taldeak = json.musikasten_vs_badok(taldeak, site)

ag.change_errore_fitx('./logs/exekuzio_erroreak.log')

sartutakoak=[]
for taldea in taldeak:
	try:
		funtzioak.taldeaOsatuKodearekin(site, taldea['item_kodea'], taldea)
		sartutakoak.append(taldea)
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + taldea['izena'] + ' (' +taldea['item_kodea'] + ') ---> ERROREA EGON DA \n')


file=open('./musikastenID/sartutakoak.json', 'w')
json.dumps(sartutakoak, file )