# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:54:46 2023

@author: anepa
"""
import pywikibot
import traceback
import pwbFuntzioak
import csvreader as c
import csv

def wikidatanDago(taldeIzena):
    # Bilatu talde izena wikidatan
    wikidata_site = pywikibot.Site('wikidata', 'wikidata')
    search_results = wikidata_site.search_entities(taldeIzena, language = 'eu')
    
    # Izen bera duen orririk aurkitu bada
    if(search_results != None):
        for result in search_results:
            #  Lortu wikidatako itema
            item = pywikibot.ItemPage(wikidata_site, result['id'])
            item.get()
            # Aztertu Honako Hau Da statement-a
            if result['label'] == taldeIzena:
                 return item.id
    return None

def aztertuHonakoHauDa(wds, item):
    
    musOrganizationQ = 'Q2088357'
    humanQ = 'Q5'
    # Honako Hau Da statement-a badu? (pwdFuntzioak fitxategitik)
    baduHonakoHauDa = pwbFuntzioak.statementHoriDu(wds, item.id, 'P31')
    if baduHonakoHauDa:
        #  Lortu HonakoHauDa statementean dauden balioak
        statements = item.claims['P31']
        for statement in statements:
            value = statement.getTarget()
            # 'Gizakia' edo 'Music Organization bada'
            if value.id == humanQ or value.id == musOrganizationQ:
                return True
            #  'Music organization'-en azpiklasea bada
            elif is_subclass_of(value.id, musOrganizationQ):
                return True
            else:
                return False
    else:
        return False
                
def is_subclass_of(qid1, qid2):
    site = pywikibot.Site("wikidata", "wikidata")
    item1 = pywikibot.ItemPage(site, qid1)

    claims1 = item1.get()['claims'].get('P279', [])
    for claim1 in claims1:
        target1 = claim1.getTarget()
        if target1.id == qid2:
            return True

    return False
            
def herriaBadago(herriIzena):
    try:
        wikidata_site = pywikibot.Site('wikidata', 'wikidata')
        search_results = wikidata_site.search_entities(herriIzena, language = 'eu')
        if(search_results != None):
            for result in search_results:
                item = pywikibot.ItemPage(wikidata_site, result['id'])
                item.get()
                baduHonakoHauDa = pwbFuntzioak.statementHoriDu(wikidata_site, item.id, 'P31')
                if baduHonakoHauDa:
                    # prop = pywikibot.PropertyPage(wikidata_site, 'P31')
                    statements = item.claims['P31']
                    for statement in statements:
                        value = statement.getTarget()
                        if 'Q2074737' == value.id or 'Q484170' == value.id:
                            return item.id
        return None
    except Exception:
        traceback.print_exc()


def herriSinplifikatuakLortu():
	datuak = c.lortu_datuak('./datuak/taldeak.csv','./datuak/diskak.csv','./datuak/kantak.csv');
	herriLista = []
	for taldea in datuak:
		herriak = c.lortuHerriak(taldea['herria'])
		if herriak is not None:
			for herri in herriak:
				if herri not in herriLista:
					herriLista.append(herri)
				
	fileHerri=open('./herriak/herriakSinplifikatuta.csv', 'w', newline='')
	writerHerri = csv.writer(fileHerri)
	
	for i in herriLista:
		writerHerri.writerow([i])
		

