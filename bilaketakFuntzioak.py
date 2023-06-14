# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:54:46 2023

@author: anepa
"""
import pywikibot
import traceback
import pwbFuntzioak

# funtzioa
def wikidatanDago(taldeIzena):
    emaitza = False
    try:
        # Wikidataren orria jaso
        wikidata_site = pywikibot.Site('wikidata', 'wikidata')
    
        # Talde izen hori duten orriak bilatu
        search_results = wikidata_site.search_entities(taldeIzena, language='eu')
        
        # print the search results
        # emaitza = []
        # emaitzak = []
        if(search_results != None):
            for result in search_results:
                item = pywikibot.ItemPage(wikidata_site, result['id']) 
                item.get()
                try:
                    label = item.labels['eu'] # Euskerazko atalean badu izenbururik?
                    emaitza = True
                except KeyError:
                    # label = 'KeyError'
                    emaitza = False
            
            # for result in search_results:
            #     print(result['label'])


        # if(search_results != None): # Orriren bat badago
        #     for result in search_results:
        #         item = pywikibot.ItemPage(wikidata_site, result['id']) 
        #         item.get()
        #         try:
        #             label = item.labels['eu'] # Euskerazko atalean badu izenbururik?
        #         except KeyError:
        #             label = 'KeyError'
                
        #         try:
        #             description = item.descriptions['eu'] # Euskerazko atalean badu deskribapenik?
        #         except:
        #             description = 'KeyError'
        #         emaitza = [item.id, label, description] # Orri hau
        #         emaitzak.append(emaitza) # Taldeak dituen orri guztien bektorea
        # else: # Ez badago orririk
        #     emaitza = ['EzDago', taldeIzena, '']
        return emaitza
    except Exception:
        traceback.print_exc()


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
                    
                
            
            
    