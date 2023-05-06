# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:44:58 2023

@author: Anekoldolorea
"""

import pywikibot
import aldagaiGlobalak as ag
import csv


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
		label= {"eu": izena+'(r)en albumak orden kronologikoan', "es":"Álbumes de "+ izena + " en orden cronológico", "en": izena + "'s albums in chronological order"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Wikimedia albums discography", "es":"Discografía de álbumes de Wikimedia", "eu": "Wikimediako albumen diskografia"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==4: #taldearen albumak sortu
		label= {"eu": izena + " (albuma)", "en": izena +" (album)", "es": izena +" (album)"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":taldeIzena+"'s album", "es":"Álbum de "+ taldeIzena , "eu": taldeIzena + "(r)en albuma"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==5: #taldearen single diskografia sortu
		label= {"eu": izena+'ren sinlge diskografia', "en": izena + "'s singles discography", "es": "Discografía de singles de " + izena}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Wikimedia singles discography", "es":"Discografía de sinlges de Wikimedia", "eu": "Wikimediako single diskografia"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==6: #talde baten sinlgeak
		label= {"eu": izena+ " (single)", "en": izena + " (single)", "es": izena +" (single)"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":taldeIzena+"'s single", "es":"Single de "+ taldeIzena, "eu": taldeIzena +"(r)en single-a"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	return new_item.getID()


def add_statement(site, itemCode, statementCode,targetCode, reference = None):
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
		if reference is not None:
			ref_url = pywikibot.Claim(repo, 'P94578')
			ref_url.setTarget(reference)
			claim.addSources([ref_url])
		item.addClaim(claim, summary=u'Statement added')




def add_dateStatement(site, itemCode, statementCode,year): #sorrera edo jaiotze data gehitzeko
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	
	item.get()  # you need to call it to access any data.
	if statementCode in item.claims: #sorrera data dagoeneko baldin badago ez dugu aldatuko
		pywikibot.output(u'Error:Target already exist')
	else:
		dateclaim = pywikibot.Claim(repo,statementCode)
		dateOfBirth = pywikibot.WbTime(year=year)
		dateclaim.setTarget(dateOfBirth)
		item.addClaim(dateclaim, summary=u'Adding date')
		
		

def add_reference(site, itemCode, statementCode, url):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	
	item.get()  # you need to call it to access any data.
	if statementCode in item.claims: # instance of
		pywikibot.output(u'Error:Target already exist')
	else:
		urlclaim = pywikibot.Claim(repo,statementCode)
		urlclaim.setTarget(url)
		item.addClaim(urlclaim, summary=u'Adding URL reference')


def get_statement_codes(site, itemCode):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	item_dict = item.get()
	clm_dict = item_dict["claims"]
	return clm_dict




"""
	funtzioak klaseko  __taldearen_informazioa_lortu(url, datuak) funtzioak itzultzen duen datuak
	parametro gisa sartzea da asmoa
	
	GENEROEKIN ARAZOA: LEHENIK ETA BEHIN GENERO HORIEN KODEA ESKURATU BEHAR DUGU WIKIDATATIK
	"""
def taldeBerriaSortu(site, datuak):
	itemKodea = create_item(site,datuak['izena'],1,'')
	add_statement(site,itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['musika talde'])
	if(datuak['urtea']!=''):
		add_dateStatement(site, itemKodea, ag.KODEAK['sorrera data'],int(datuak['urtea']))
	diskografiaKodea=taldeBatenDiskografiaSortu(site,datuak['izena'], datuak['diskak'], itemKodea)
	add_statement(site, itemKodea, ag.KODEAK['diskografia'], diskografiaKodea)
	#for i in len(datuak['generoak']):
	#	add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK(datuak[i]['generoak']))
	add_reference(site, itemKodea, ag.KODEAK['url erreferentzia'], datuak['url'])






def taldeBatenDiskografiaSortu(site, izena,diskoak, taldeKodea):
	itemKodea=create_item(site, izena,2,'')
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['wikimedia artist discography'])
	albumakOrdenKronoKode = taldeBatenAlbumakOrdenKronologikoan(site,izena, itemKodea, diskoak, taldeKodea)
	add_statement(site, itemKodea, ag.KODEAK['elementuaren zerrenda'],albumakOrdenKronoKode)
	singleDiskografiaKode= taldeBatenSingleDiskografia(site,izena, itemKodea, diskoak, taldeKodea)
	add_statement(site, itemKodea, ag.KODEAK['elementuaren zerrenda'],singleDiskografiaKode)
	return itemKodea




def taldeBatenAlbumakOrdenKronologikoan(site,izena,diskografiaKodea, diskak, taldeKodea):
	itemKodea=create_item(site,izena,3,'')
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['wikimedia albums discography'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskografiaKodea)
	for i in range(len(diskak)):
		if(diskak[i]['single'] is False):
			kodeLag=taldeBatenAlbumakSortu(site,diskak[i]['izena'], taldeKodea, itemKodea, diskak)
			add_statement(site, itemKodea, ag.KODEAK['osatuta'],kodeLag)
	add_statement(site, itemKodea, ag.KODEAK['honen zerrenda'], ag.KODEAK['album'])
	return itemKodea







"""
	ALBUMAREN GENERO ARTISTIKOA LORTZEA FALTA DA
"""
def taldeBatenAlbumakSortu(site,izena,taldeKodea,albumakOrdenKronoKode, diskak):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, taldeKodea)
	item_dict=item.get()
	itemKodea=create_item(site, izena,4, item_dict["labels"]["eu"])
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['album'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], albumakOrdenKronoKode)
	add_statement(site, itemKodea, ag.KODEAK['interpretatzailea'], taldeKodea)
	add_statement(site, itemKodea, ag.KODEAK['lanaren edo izenaren hizkuntza'], ag.KODEAK['euskara'])
	for i in len(diskak['generoa']):
		add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'],ag.GENEROAK(diskak[i]['generoa']))
	if diskak['urtea'] != '':
		add_dateStatement(site, itemKodea, ag.KODEAK['argitaratze data'],int(diskak['urtea']))
	return itemKodea








def taldeBatenSingleDiskografia(site,izena,diskografiaKodea, diskak, taldeKodea):
	itemKodea=create_item(site,izena,5,'')
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['singles discography'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskografiaKodea)
	for i in range(len(diskak)):
		if(diskak[i]['single'] is True):
			kodeLag= taldeBatenSingleakSortu(site,diskak[i]['izena'], itemKodea, taldeKodea, int(diskak[i]['urtea']))
			add_statement(site, itemKodea, ag.KODEAK['osatuta'],kodeLag)
	return itemKodea



def taldeBatenSingleakSortu(site,izena, singleDiskografiaKodea, taldeKodea, data):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, taldeKodea)
	item_dict=item.get()
	itemKodea=create_item(site, izena,6,  item_dict["labels"]["eu"])
	add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['single'])
	add_statement(site, itemKodea, ag.KODEAK['honen parte da'], singleDiskografiaKodea)
	add_reference(site, itemKodea, ag.KODEAK['izenburua'],izena)
	add_statement(site, itemKodea, ag.KODEAK['interpretatzailea'], taldeKodea)
	if(data!=''):
		add_dateStatement(site, itemKodea, ag.KODEAK['argitaratze data'],data)
	return itemKodea


#BERDINA BAINA KODEETATIK ABIATUZ

def taldeaOsatuKodearekin(site,itemKodea, datuak):
	add_statement(site,itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['musika talde'])
	if(datuak['urtea']!=''):
		add_dateStatement(site, itemKodea, ag.KODEAK['sorrera data'],int(datuak['urtea']))
	
	diskografiaKodea=taldeBatenDiskografiaSortu(site,datuak['izena'], datuak['diskak'], itemKodea)
	add_statement(site, itemKodea, ag.KODEAK['diskografia'], diskografiaKodea)
	for i in len(datuak['generoak']):
		add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'],ag.GENEROAK(datuak[i]['generoak']))
	add_reference(site, itemKodea, ag.KODEAK['url erreferentzia'], datuak['url'])




def csv_to_dict(taldeak, diskak):
	with open(taldeak, mode='r') as taldeak_csv:
		taldeakCsv_reader = csv.DictReader(taldeak_csv)
		datuak = {}
		for row in taldeakCsv_reader:
			datuak['id'] = row[0]
			datuak['izena']=row[1]
			datuak['url']=row[2]
	with open(diskak, mode='r') as diskak_csv:
		diskakCsv_reader = csv.DictReader(diskak_csv)
		for row in diskakCsv_reader:
			if(row[4]==datuak['id']):
				datuak['diska']['izena']=row[1]
				datuak['diska']['url']=row[2]
				datuak['diska']['generoa']=row[3]
	return datuak




