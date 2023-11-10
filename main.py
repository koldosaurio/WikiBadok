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

#11 arte gehitu dugu
sartutakoak=[]
for taldea in taldeak[:12]:
	try:
		funtzioak.taldeaOsatuKodearekin(site, taldea['item_kodea'], taldea)
		sartutakoak.append(taldea)
	except:
		funtzioak.arazoa_tratatu(dt.now().strftime("%H:%M:%S") + taldea['izena'] + " (" +str(taldea['item_kodea']) + ") ---> ERROREA EGON DA \n")


if sartutakoak != []:
	json.dump(json.dumps(sartutakoak), open("./musikastenID/sartutakoak.json", "a"))

ag.ERRORE_FITX.close()



