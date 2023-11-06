# -*- coding: utf-8 -*-
import pwbFuntzioak as p
import json
import pywikibot as pwb
import aldagaiGlobalak as ag

taldeak = json.loads(json.load(open("./musikastenID/taldeak_alderatuta.json", 'r')))
taldea = taldeak[0]
em = []
for diska in taldea['diskak']:
	lag=p.__badagoDiska(pwb.Site("wikidata", "wikidata"), diska, taldea['item_kodea'], ag.KODEAK['album'])
	if lag !=0 and lag is not None:
		em.append(lag)