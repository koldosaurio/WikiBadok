# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:54:46 2023

@author: anepa
"""
import pywikibot

def wikidatanDago(site, taldeIzena):

    emaitza = []
    print(f"TALDEA: {taldeIzena} ")
    try:
        item = pywikibot.ItemPage.fromPage(pywikibot.Page(site, taldeIzena))
        label = item.labels.get("eu")
        description = item.descriptions.get("eu")
        emaitza = [item, label, description]
        # if("musika taldea" in description):
        #     print(f"KODEA: {item}")
        # else:
        #     print("Ez da euskal musika taldea")
        #     print(f"DESCRIPTION: {description}")
    except:
        print(" Ez dago wikidatan")
    print("\n")
    return emaitza
    