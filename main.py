3# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 18:49:06 2023

@author: Lorea
"""

import pwbFuntzioak as funtzioak
import pywikibot as pwb
import json_to_dict as jtd
import csvreader as csv
import aldagaiGlobalak as ag
from datetime import datetime as dt
import json


site = pwb.Site("wikidata", "wikidata")

# taldeak = csv.lortu_datuak()
# taldeak = jtd.musikasten_vs_badok(taldeak, site)

taldeak = json.loads(json.load(open("./musikastenID/taldeak_alderatuta.json", 'r')))

#ag.change_errore_fitx('./logs/exekuzio_erroreak.log')

sartutakoak=[]
for taldea in taldeak[:1]:
	
	try:
		funtzioak.taldeaOsatuKodearekin(site, taldea['item_kodea'], taldea)
		sartutakoak.append(taldea)
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + taldea['izena'] + ' (' +taldea['item_kodea'] + ') ---> ERROREA EGON DA \n')


if sartutakoak != []:
 	json.dump(json.dumps(sartutakoak), open('./musikastenID/sartutakoak.json', 'a'))


