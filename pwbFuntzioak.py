# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:44:58 2023

@author: Lorea
"""

import pywikibot
site = pywikibot.Site("wikidata", "wikidata")


def create_item(site,izena):
	new_item = pywikibot.ItemPage(site)
	label= {"en": izena, "es": izena, "eu": izena} #agian "(musika taldea)" gehitu izenaren ondoan
	new_item.editLabels(labels=label, summary="Label-ak gehitu")
	# Add description here or in another function
	return new_item.getID()


#def add_statement(item, claim, target):
 #   site = pywikibot.Site("wikidata", "wikidata")
  #  repo = site.data_repository()
   # claim.setTarget(target)
    #item.addClaim(claim, summary=u'Ispiluaren aurrean albuma honako hau da: album')

