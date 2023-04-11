# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:44:58 2023

@author: Anekoldolorea
"""

import pywikibot
site = pywikibot.Site('wikidata:test')


def create_item(site,izena):
	new_item = pywikibot.ItemPage(site)
	label= {"en": izena, "es": izena, "eu": izena}
	new_item.editLabels(labels=label, summary="Label-ak gehitu")
	#description={"en":"Basque musician(s)", "es":"Músico(s) Vascos", "eu": "Euskal musikaria(k)"}
	#new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
	return new_item.getID()


def add_statement(site, itemCode, statementCode,targetCode):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	claim = pywikibot.Claim(repo,statementCode) #honako hau da
	target = pywikibot.ItemPage(repo,targetCode) #album	

	item.get()  # you need to call it to access any data.

	if statementCode in item.claims: # instance of
		if targetCode is item.claims[statementCode][0].getTarget(): #statement eta target egokiak dagoeneko baditu
			pywikibot.output(u'Error:Target already exist')
		else:  #Statement-a badu baina guk nahi dugun balioa ez
			item.claims[statementCode][0].setTarget(target)
			item.addClaim(claim, summary=u'Statement added')
	else: #statementa eta targeta gehitu behar dira
		claim.setTarget(target) #Set the target value in the local object.
		item.addClaim(claim, summary=u'Statement added')



def add_dateStatement(site, itemCode, statementCode,year): #sorrera edo jaiotze data gehitzeko
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	
	item.get()  # you need to call it to access any data.
	if statementCode in item.claims: # instance of
		pywikibot.output(u'Error:Target already exist')
	else:
		dateclaim = pywikibot.Claim(repo,statementCode)
		dateOfBirth = pywikibot.WbTime(year=year)
		dateclaim.setTarget(dateOfBirth)
		item.addClaim(dateclaim, summary=u'Adding date')



def add_reference(site, itemCode, statementCode, targetCode,web):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	
	item.get()
	item.editclaim(statementCode, targetCode, refs={(web)})
