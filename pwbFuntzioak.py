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
	item_dict = item.get()
	clm_dict = item_dict["claims"]	#statement guztien lista lortu
	found = False
	if statementCode in clm_dict:
		clm_list = clm_dict[statementCode]	#lista horretatik guk nahi dugun statementa aztertu
		for clm in clm_list: #guk esandako statementeko target guztiak aztertuko ditugu gurea dagoeneko badagoen aztertzeko
			clm_target = clm.getTarget()
			targetId = clm_target.id
			if targetId.__eq__(targetCode):
				pywikibot.output(u'Error:Target already exist')
				found=True
			break
	if(not found):
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
