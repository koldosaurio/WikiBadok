# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:54:46 2023

@author: anepa
"""
import pywikibot
import traceback

# funtzioa
def wikidatanDago(taldeIzena):
    try:
        # Wikidataren orria jaso
        wikidata_site = pywikibot.Site('wikidata', 'wikidata')
    
        
        # Talde izen hori duten orriak bilatu
        search_results = wikidata_site.search_entities(taldeIzena, language='eu')
        
        # print the search results
        # emaitza = []
        # emaitzak = []
        if(search_results == None):
            return False;
        else:
            return True;
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
    except Exception:
        traceback.print_exc()
    return False;


            
    