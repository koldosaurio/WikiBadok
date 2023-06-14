# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:44:58 2023

@author: Anekoldolorea
"""

import pywikibot
import aldagaiGlobalak as ag
import csvreader as c


def create_item(site,izena, mota,taldeIzena):
	new_item = pywikibot.ItemPage(site)
	
	if mota==1: #taldea sortu
		label= {"eu": izena, "en": izena, "es": izena}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Basque music band", "es":"Grupo de música vasco", "eu": "Euskal musika taldea"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==2: #taldearen diskografia sortu
		label= {"eu": izena +'(r)en diskografia', "en":izena+"'s discography", "es": "Discografía de "+izena}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Wikimedia artist discography", "es":"Discografía de un artista o grupo musical de Wikimedia", "eu": "Wikimediako artista edo musika taldearen diskografia"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==3:#taldearen album diskografia sortu
		label= {"eu": izena+'(r)en albumak', "es":"Álbumes de "+ izena, "en": izena + "'s albums"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Wikimedia albums discography", "es":"Discografía de álbumes de Wikimedia", "eu": "Wikimediako albumen diskografia"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==4: #taldearen albumak sortu
		label= {"eu": izena + " (albuma)", "en": izena +" (album)", "es": izena +" (album)"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":taldeIzena+"'s album", "es":"Álbum de "+ taldeIzena , "eu": taldeIzena + "(r)en albuma"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==5: #taldearen single diskografia sortu
		label= {"eu": izena+'(r)en sinlge diskografia', "en": izena + "'s singles discography", "es": "Discografía de singles de " + izena}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Wikimedia singles discography", "es":"Discografía de sinlges de Wikimedia", "eu": "Wikimediako single diskografia"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==6: #talde baten sinlgeak
		label= {"eu": izena+ " (single)", "en": izena + " (single)", "es": izena +" (single)"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":taldeIzena+"'s single", "es":"Single de "+ taldeIzena, "eu": taldeIzena +"(r)en single-a"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	return new_item.getID()


def add_statementTaldeKodearekin(site, itemCode, statementCode,targetCode, reference = None, referenceCode = None):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	claim = pywikibot.Claim(repo,statementCode)
	target = pywikibot.ItemPage(repo,targetCode) 
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
		if reference is not None:
			ref_url = pywikibot.Claim(repo, referenceCode)
			ref_url.setTarget(reference)
			claim.addSources([ref_url])
		item.addClaim(claim, summary=u'Statement added')

def add_statement(site, itemCode, statementCode,targetCode, reference = None, referenceCode = None):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	claim = pywikibot.Claim(repo,statementCode)
	target = pywikibot.ItemPage(repo,targetCode)
	
	claim.setTarget(target) #Set the target value in the local object.
	if reference is not None:
		ref_url = pywikibot.Claim(repo, referenceCode)
		ref_url.setTarget(reference)
		claim.addSources([ref_url])
	item.addClaim(claim, summary=u'Statement added')


def add_dateStatementTaldeKodearekin(site, itemCode, statementCode,year, reference = None, referenceCode = None): #sorrera edo jaiotze data gehitzeko
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	
	item.get()  # you need to call it to access any data.
	if statementCode in item.claims: #sorrera data dagoeneko baldin badago ez dugu aldatuko
		pywikibot.output(u'Error:Target already exist')
	else:
		dateclaim = pywikibot.Claim(repo,statementCode)
		dateOfBirth = pywikibot.WbTime(year=year)
		dateclaim.setTarget(dateOfBirth)
		if reference is not None:
			ref_url = pywikibot.Claim(repo, referenceCode)
			ref_url.setTarget(reference)
			dateclaim.addSources([ref_url])
		item.addClaim(dateclaim, summary=u'Adding date')
		

def add_dateStatement(site, itemCode, statementCode,year, reference = None, referenceCode = None):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)

	dateclaim = pywikibot.Claim(repo,statementCode)
	dateOfBirth = pywikibot.WbTime(year=year)
	dateclaim.setTarget(dateOfBirth)
	if reference is not None:
		ref_url = pywikibot.Claim(repo, referenceCode)
		ref_url.setTarget(reference)
		dateclaim.addSources([ref_url])
	item.addClaim(dateclaim, summary=u'Adding date')



def statementHoriDu(site, itemCode, statementCode):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	item.get()
	if statementCode in item.claims:
		return True
	else:
		return False










"""
----------------------TALDEAK SORTUTA EZ DAUDENEAN ERABILTZEKO METODOA: taldeBerriaSortu()-----------------
"""

#TODO herria sartu

"""
Metodo honek hiztegi bat jasota talde berria sortuko du oso osorik
(diskografia itema sortuz, horren barruan album eta single-en diskografiaren itemak sortuz 
 eta single eta albumen itemak sortuz)
"""
def taldeBerriaSortu(site, talde):
	itemKodea = create_item(site,talde['izena'],1,'')
	add_statement(site,itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['musika talde'])
	urteak= c.lortuUrteak(talde['urtea'])
	if(urteak is not None):
		if(len(urteak)==1):
			add_dateStatement(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],talde['url'] , ag.KODEAK['url'])
		else:
			add_dateStatement(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],talde['url'] , ag.KODEAK['url'])
			add_dateStatement(site, itemKodea, ag.KODEAK['bukaera data'],urteak[1],talde['url'] , ag.KODEAK['url'])
	diskografiaKodea=taldeBatenDiskografiaSortu(site,talde, itemKodea)
	add_statement(site, itemKodea, ag.KODEAK['diskografia'], diskografiaKodea)
	generoak= c.lortuGeneroak(talde['generoak'])
	if generoak is not None:
		for genero in generoak:
			add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK(genero), talde['url'] , ag.KODEAK['url'])
	return itemKodea



def taldeBatenDiskografiaSortu(site, talde, taldeKodea):
	itemKodea=create_item(site, talde['izena'],2,'')
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['wikimedia artist discography'])
	albumakOrdenKronoKode = taldeBatenAlbumakOrdenKronologikoan(site,itemKodea, talde, taldeKodea)
	add_statement(site, itemKodea, ag.KODEAK['elementuaren zerrenda'],albumakOrdenKronoKode)
	singleDiskografiaKode= taldeBatenSingleDiskografia(site,itemKodea, talde, taldeKodea)
	add_statement(site, itemKodea, ag.KODEAK['elementuaren zerrenda'],singleDiskografiaKode)
	return itemKodea




def taldeBatenAlbumakOrdenKronologikoan(site,diskografiaKodea, talde, taldeKodea):
	itemKodea=create_item(site,talde['izena'],3,'')
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['wikimedia albums discography'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskografiaKodea)
	for diska in talde['diskak']:
		if(diska['single']=='False'):
			kodeLag=taldeBatenAlbumakSortu(site,diska, taldeKodea, itemKodea, talde)
			add_statement(site, itemKodea, ag.KODEAK['osatuta'],kodeLag, diska['url'] , ag.KODEAK['url'])
	add_statement(site, itemKodea, ag.KODEAK['honen zerrenda'], ag.KODEAK['album'])
	return itemKodea



def taldeBatenAlbumakSortu(site,diska,taldeKodea,albumakOrdenKronoKode, talde):
	itemKodea=create_item(site, diska['izena'],4, talde['izena'])
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['album'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], albumakOrdenKronoKode)
	add_statement(site, itemKodea, ag.KODEAK['interpretatzailea'], taldeKodea)
	add_statement(site, itemKodea, ag.KODEAK['lanaren edo izenaren hizkuntza'], ag.KODEAK['euskara'])
	generoak = c.lortuGeneroak(diska['generoa'])
	if generoak is not None:
		for genero in generoak:
			add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'],ag.GENEROAK(genero))
	urtea= c.lortuUrteak(diska['urtea'])
	if urtea is not None:
		add_dateStatement(site, itemKodea, ag.KODEAK['argitaratze data'],urtea[0], diska['url'] , ag.KODEAK['url'])
	return itemKodea



def taldeBatenSingleDiskografia(site,diskografiaKodea, talde, taldeKodea):
	itemKodea=create_item(site,talde['izena'],5,'')
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['singles discography'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskografiaKodea)
	for diska in talde['diskak']:
		if(diska['single']=='True'):
			kodeLag= taldeBatenSingleakSortu(site,diska, itemKodea, taldeKodea, talde)
			add_statement(site, itemKodea, ag.KODEAK['osatuta'],kodeLag)
	add_statement(site, itemKodea, ag.KODEAK['honen zerrenda'], ag.KODEAK['single'])
	return itemKodea


def taldeBatenSingleakSortu(site,diska, singleDiskografiaKodea, taldeKodea, talde):
	itemKodea=create_item(site, diska['izena'],6,talde['izena'])
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['single'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], singleDiskografiaKodea)
	add_statement(site, itemKodea, ag.KODEAK['interpretatzailea'], taldeKodea, diska['url'] , ag.KODEAK['url'])
	add_statement(site, itemKodea, ag.KODEAK['lanaren edo izenaren hizkuntza'], ag.KODEAK['euskara'])
	urtea= c.lortuUrteak(diska['urtea'])
	if urtea is not None:
		add_dateStatement(site, itemKodea, ag.KODEAK['argitaratze data'],urtea[0], diska['url'] , ag.KODEAK['url'])
	return itemKodea








"""
-------------TALDEA SORTUTA BADAGO ERABILI BEHARKO DEN METODOA: taldeaOsatuKodearekin----------
"""

def taldeaOsatuKodearekin(site,itemKodea, talde):
	add_statementTaldeKodearekin(site,itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['musika talde'])
	urteak= c.lortuUrteak(talde['urtea'])
	if(urteak is not None):
		if(len(urteak)==1):
			add_dateStatementTaldeKodearekin(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],talde['url'] , ag.KODEAK['url'])
		else:
			add_dateStatementTaldeKodearekin(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],talde['url'] , ag.KODEAK['url'])
			add_dateStatementTaldeKodearekin(site, itemKodea, ag.KODEAK['bukaera data'],urteak[1],talde['url'] , ag.KODEAK['url'])
	baduDiskografia= statementHoriDu(site, itemKodea, ag.KODEAK['diskografia'])
	if baduDiskografia:
		raise Exception(itemKodea + " kodea duen taldeak badu diskografia. Talde izena :"+ talde[['izena']])
	else:
		diskografiaKodea=taldeBatenDiskografiaSortu(site,talde, itemKodea)
		add_statement(site, itemKodea, ag.KODEAK['diskografia'], diskografiaKodea)
		generoak= talde['generoak']
		if generoak is not None:
			for genero in generoak:
				add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()], talde['url'] , ag.KODEAK['url'])