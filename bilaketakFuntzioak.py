# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:54:46 2023

@author: anepa
"""
import pywikibot
import traceback
import pwbFuntzioak


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
            if aztertuHonakoHauDa(wikidata_site, item):
                return(item.id)               

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
# funtzioa
# def wikidatanDago(taldeIzena):
#     emaitza = False
#     try:
#         # Wikidataren orria jaso
#         wikidata_site = pywikibot.Site('wikidata', 'wikidata')
    
#         # Talde izen hori duten orriak bilatu
#         search_results = wikidata_site.search_entities(taldeIzena, language='eu')
        
#         # print the search results
#         # emaitza = []
#         # emaitzak = []
#         if(search_results != None):
#             for result in search_results:
#                 item = pywikibot.ItemPage(wikidata_site, result['id']) 
#                 item.get()
#                 try:
#                     label = item.labels['eu'] # Euskerazko atalean badu izenbururik?
#                     emaitza = True
#                 except KeyError:
#                     # label = 'KeyError'
#                     emaitza = False
            
#             # for result in search_results:
#             #     print(result['label'])


#         # if(search_results != None): # Orriren bat badago
#         #     for result in search_results:
#         #         item = pywikibot.ItemPage(wikidata_site, result['id']) 
#         #         item.get()
#         #         try:
#         #             label = item.labels['eu'] # Euskerazko atalean badu izenbururik?
#         #         except KeyError:
#         #             label = 'KeyError'
                
#         #         try:
#         #             description = item.descriptions['eu'] # Euskerazko atalean badu deskribapenik?
#         #         except:
#         #             description = 'KeyError'
#         #         emaitza = [item.id, label, description] # Orri hau
#         #         emaitzak.append(emaitza) # Taldeak dituen orri guztien bektorea
#         # else: # Ez badago orririk
#         #     emaitza = ['EzDago', taldeIzena, '']
#         return emaitza
#     except Exception:
#         traceback.print_exc()

                    
                
            
            
    