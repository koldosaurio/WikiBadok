# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:44:58 2023

@author: Anekoldolorea
"""

import pywikibot
import aldagaiGlobalak as ag
import csvreader as c
from datetime import datetime as dt
from pywikibot import pagegenerators






def __create_item(site,izena, mota,taldeIzena):
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
		label= {"eu": izena+'(r)en single diskografia', "en": izena + "'s singles discography", "es": "Discografía de singles de " + izena}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":"Wikimedia singles discography", "es":"Discografía de singles de Wikimedia", "eu": "Wikimediako single diskografia"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	elif mota==6: #talde baten singleak
		label= {"eu": izena+ " (single)", "en": izena + " (single)", "es": izena +" (single)"}
		new_item.editLabels(labels=label, summary="Label-ak gehitu")
		description={"en":taldeIzena+"'s single", "es":"Single de "+ taldeIzena, "eu": taldeIzena +"(r)en single-a"}
		new_item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		
	return new_item.getID()





def __add_badokStatement(site, itemCode, target):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	claim = pywikibot.Claim(repo,ag.KODEAK['badok'])

	item_dict = item.get()
	clm_dict = item_dict["claims"]	#statement guztien lista lortu
	found = False
	if ag.KODEAK['badok'] in clm_dict:
		pywikibot.output(u'Error:Target already exist')
		found=True
	if not found:
		claim.setTarget(target) #Set the target value in the local object.
		item.addClaim(claim, summary=u'Statement added')





def __add_statementTaldeKodearekin(site, itemCode, statementCode,targetCode, reference = None, referenceCode = None):
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

def __add_statement(site, itemCode, statementCode,targetCode, reference = None, referenceCode = None):
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


def __add_dateStatementTaldeKodearekin(site, itemCode, statementCode,year,statementCode2=None, reference = None, referenceCode = None): #sorrera edo jaiotze data gehitzeko
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	
	item.get()  # you need to call it to access any data.
	if(statementCode2 is not None):
		if (statementCode or statementCode2)in item.claims: #sorrera data dagoeneko baldin badago ez dugu aldatuko
			pywikibot.output(u'Error:Target already exist')
			return None
	elif(statementCode2 is None):
		if statementCode in item.claims: #sorrera data dagoeneko baldin badago ez dugu aldatuko
			pywikibot.output(u'Error:Target already exist')
			return None
	dateclaim = pywikibot.Claim(repo,statementCode)
	dateOfBirth = pywikibot.WbTime(year=year)
	dateclaim.setTarget(dateOfBirth)
	if reference is not None:
		ref_url = pywikibot.Claim(repo, referenceCode)
		ref_url.setTarget(reference)
		dateclaim.addSources([ref_url])
	item.addClaim(dateclaim, summary=u'Adding date')


def __add_dateStatement(site, itemCode, statementCode,year, reference = None, referenceCode = None):
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



def __statementHoriDu(site, itemCode, statementCode):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, itemCode)
	item.get()
	if statementCode in item.claims:
		return True
	else:
		return False


def __gehitu_herria(site, itemKodea, talde, herriak):
	#SALBUESPENAK
	for herria in herriak:
		if herria == 'Urretxu-Zumarraga':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Urretxu'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Zumarraga'], talde['url'] , ag.KODEAK['url'])
		
		elif herria == 'Oiartzun -Donostia':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Oiartzun'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Donostia'], talde['url'] , ag.KODEAK['url'])
	
		elif herria == 'Azpeitia-Zarautz':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Azpeitia'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Zarautz'], talde['url'] , ag.KODEAK['url'])
	
		elif herria == 'Beskoitze -Bilbo':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Beskoitze'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Bilbo'], talde['url'] , ag.KODEAK['url'])
	
		elif herria == 'Iruñea-Donostia-Bilbo':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Iruñea'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Donostia'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Bilbo'], talde['url'] , ag.KODEAK['url'])
			
		elif herria == 'Ziburu-Donibane Lohizune' or herriak == 'Donibane-Ziburu':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Donibane Lohizune'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Ziburu'], talde['url'] , ag.KODEAK['url'])
	
		elif herria == 'Uztaritze -Tolosa':
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Uztaritze'], talde['url'] , ag.KODEAK['url'])
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK['Tolosa'], talde['url'] , ag.KODEAK['url'])
		
		else:
			__add_statement(site, itemKodea, ag.KODEAK['eraketa lekua'], ag.HERRIAK[herria], talde['url'] , ag.KODEAK['url'])





def __taldeBatenDiskografiaSortu(site, talde, taldeKodea):
	itemKodea = None
	try:
		itemKodea=__create_item(site, talde['izena'],2,'')
		try:
			__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['wikimedia artist discography'])
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIAN HONAKO HAU DA GEHITZEAN\n')
		
		albumakOrdenKronoKode = __taldeBatenDiskoDiskografiaSortu(site,itemKodea, talde, taldeKodea, False)
		if albumakOrdenKronoKode[0] is not None:
			try:
				__add_statement(site, itemKodea, ag.KODEAK['elementuaren zerrenda'],albumakOrdenKronoKode[0])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIAN ELEMENTUAREN ZERRENDA:album diskografia GEHITZEAN\n')

			if albumakOrdenKronoKode[1]:
				singleDiskografiaKode= __taldeBatenDiskoDiskografiaSortu(site,itemKodea, talde, taldeKodea, True)
				if singleDiskografiaKode[0] is not None:
					try:
						__add_statement(site, itemKodea, ag.KODEAK['elementuaren zerrenda'],singleDiskografiaKode[0])
					except:
						ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIAN ELEMENTUAREN ZERRENDA:single diskografia GEHITZEAN\n')
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIA SORTZEAN; EZ DA SORTU ETA EZ DA TALDEAN GEHITU\n')

	return itemKodea


def __taldeBatenDiskoDiskografiaSortu(site, diskografiaKodea, talde, taldeKodea, single):
	sortuSingle = False
	itemKodea=None
	if single:
		non = 'SINGLE'
	else:
		non = 'ALBUM'
	
	if not single:#albumen diskografia sortu behar dugu
		try:
			itemKodea = __create_item(site, talde['izena'], 3, '')  # Album diskografia sortu
			try:
				__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['wikimedia albums discography'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN ALBUM DISKOGRAFIAN HONAKO HAU DA GEHITZEAN\n')

		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diskografiaKodea + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIAN ALBUM DISKOGRAFIA SORTZEAN; EZ DA SORTU ETA EZ DA DISKOGRAFIAN GEHITU (SINLGE DISKOGRAFIA EZ DA SORTUKO)\n')

	else:#single diskografia sortu behar dugu
		try:
			itemKodea=__create_item(site,talde['izena'],5,'')
			try:
				__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['singles discography'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN SINGLE DISKOGRAFIAN HONAKO HAU DA GEHITZEAN\n')

		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diskografiaKodea + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIAN SINGLE DISKOGRAFIA SORTZEAN; EZ DA SORTU ETA EZ DA DISKOGRAFIAN GEHITU\n')

	
	if itemKodea is not None:
		try:
			__add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskografiaKodea)
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN '+ non +' DISKOGRAFIAN HONEN PARTE DA GEHITZEAN\n')

		for diska in talde['diskak']:
			if not single and diska['single'] == 'False':

				badagoDiskaKodea = __badagoDiska(site, diska, taldeKodea, ag.KODEAK['album'])
				if badagoDiskaKodea!=0:
					if badagoDiskaKodea is None:
						kodeLag = __taldeBatenDiskaSortu(site, diska, taldeKodea, itemKodea, talde, False)
						if kodeLag is not None:
							try:
								__add_statement(site, itemKodea, ag.KODEAK['osatuta'], kodeLag, diska['url'], ag.KODEAK['url'])
							except:
								ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN '+ non +' DISKOGRAFIAN OSATUTA GEHITZEAN\n')

					else:
						__taldeBatenDiskaAldatu(site, diska, taldeKodea, itemKodea, talde, badagoDiskaKodea, False)
						try:
							__add_statement(site, itemKodea, ag.KODEAK['osatuta'], badagoDiskaKodea, diska['url'], ag.KODEAK['url'])
						except:
							ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN '+ non +' DISKOGRAFIAN OSATUTA GEHITZEAN\n')


			elif single and diska['single']=='True':
				badagoSingleKodea = __badagoDiska(site, diska, taldeKodea, ag.KODEAK['single'])
				if badagoSingleKodea!=0:
					if badagoSingleKodea is None:
						kodeLag = __taldeBatenDiskaSortu(site, diska, taldeKodea, itemKodea, talde, True)
						if kodeLag is not None:
							try:
								__add_statement(site, itemKodea, ag.KODEAK['osatuta'], kodeLag, diska['url'], ag.KODEAK['url'])
							except:
								ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN '+ non +' DISKOGRAFIAN OSATUTA GEHITZEAN\n')

					else:
						__taldeBatenDiskaAldatu(site, diska,itemKodea, taldeKodea, talde, badagoSingleKodea, True)
						try:
							__add_statement(site, itemKodea, ag.KODEAK['osatuta'], badagoSingleKodea, diska['url'], ag.KODEAK['url'])
						except:
							ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN '+ non +' DISKOGRAFIAN OSATUTA GEHITZEAN\n')

	
			elif diska['single']==True:
				sortuSingle==True
		try:
			__add_statement(site, itemKodea, ag.KODEAK['honen zerrenda'], ag.KODEAK['album'])
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +itemKodea + ') ---> ERROREA EGON DA TALDEAREN '+ non +' DISKOGRAFIAN HONEN ZERRENDA GEHITZEAN\n')

	return (itemKodea, sortuSingle)

def lortu_izenburua(site, item_kodea):
	try:
		item = pywikibot.ItemPage(site, item_kodea)
		# Fetch the label (title) in a specific language
		language = "eu"  # Replace with the desired language code
		title = item.get()['labels'].get(language)
		if title is None:
			language = "en"
			title = item.get()['labels'].get(language)
		if title is None:
			language = "es"
			title = item.get()['labels'].get(language)
		return title.lower().replace(" ", "")
	except:
		return ''


def __badagoDiska(site, diska, taldeKodea, singleValbum):
	try:
		query_template = """
		SELECT ?item ?itemLabel 
		WHERE {{
			SERVICE wikibase:label {{ bd:serviceParam wikibase:language "eus". }}
			?item wdt:P175 wd:{taldeKodea}.
			?item wdt:P31 wd:{singleValbum}.
		}}
		"""
		query = query_template.format(taldeKodea=taldeKodea, singleValbum=singleValbum)
		generator = pagegenerators.WikidataSPARQLPageGenerator(query, site=site)
		generator = pagegenerators.PreloadingEntityGenerator(generator)
		for item in generator:
			diska_izena=diska['izena'].lower().replace(" ", "")
			item_kodea = item.title()
			item_izena = lortu_izenburua(site, item_kodea)
			if diska_izena in item_izena:
				return item.id
		return None
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + diska['izena'] + ' (' +taldeKodea + ') ---> ERROREA EGON DA TALDEAREN DISKA WIKIDATAN BILATZEAN\n')

	return 0



def __taldeBatenDiskaAldatu(site, diska, taldeKodea, albumakOrdenKronoKode, talde, diskaKodea, single):
    # titulua aldatu eta (albuma) jarri
	try:
		if not single:
				repo = site.data_repository()
				item = pywikibot.ItemPage(repo, diskaKodea)
				label= {"eu": diska['izena'] + " (albuma)", "en":diska['izena'] +" (album)", "es": diska['izena'] +" (album)"}
				item.editLabels(labels=label, summary="Label-ak gehitu")
				description={"en":talde['izena']+"'s album", "es":"Álbum de "+ talde['izena'] , "eu": talde['izena'] + "(r)en albuma"}
				item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
		else:
			repo = site.data_repository()
			item = pywikibot.ItemPage(repo, diskaKodea)
			label= {"eu": diska['izena']+ " (single)", "en": diska['izena'] + " (single)", "es": diska['izena'] +" (single)"}
			item.editLabels(labels=label, summary="Label-ak gehitu")
			description={"en":talde['izena'] +"'s single", "es":"Single de "+ talde['izena'], "eu": talde['izena'] +"(r)en single-a"}
			item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ', '+diskaKodea+') ---> ERROREA EGON DA TALDEAREN DISKAREN DESKRIBAPENA ALDATZEAN \n')

		
	# honen parte da ... -ren albumak
	try:
		__add_statementTaldeKodearekin(site,diskaKodea, ag.KODEAK['honen parte da'], albumakOrdenKronoKode)
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ', '+diskaKodea+') ---> ERROREA EGON DA TALDEAREN DISKAREN HOONEN PARTE DA GEHITZEAN \n')

	# genero artistikoa
	generoak = c.lortuGeneroak(diska['generoa'])
	if generoak is not None:
		for genero in generoak:
			try:
				__add_statementTaldeKodearekin(site, diskaKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()],diska['url'], ag.KODEAK['url'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ', '+genero+') ---> ERROREA EGON DA TALDEAREN DISKAN GENEROA GEHITZEAN\n')
	# argitaratze-data
	urtea = c.lortuUrteak(diska['urtea'])
	if urtea is not None:
		try:
			__add_dateStatementTaldeKodearekin(site, diskaKodea, ag.KODEAK['argitaratze data'], urtea[0],None, diska['url'], ag.KODEAK['url'])
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' + diska['izena']  + ', '+ urtea[0] +') ---> ERROREA EGON DA TALDEAREN DISKAN URTEA GEHITZEAN\n')
	try:
		__add_badokStatement(site, diskaKodea, diska['url'].split('/')[--1])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ') ---> ERROREA EGON DA TALDEAREN DISKAN BADOK GEHITZEAN\n')
	return diskaKodea



def __taldeBatenDiskaSortu(site, diska, taldeKodea, diskaDiskografiaKodea, talde, single):
	itemKodea = None
	
	if single:
		try:
			itemKodea=__create_item(site, diska['izena'],6,talde['izena'])
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena'] + ') ---> ERROREA EGON DA TALDEAREN ALBUMA SORTZEAN\n')
		if itemKodea is not None:
			try:
				__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['single'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena'] + ') ---> ERROREA EGON DA TALDEAREN DISKAN HONAKO HAU DA GEHITZEAN\n')

	else:
		try:
			itemKodea = __create_item(site, diska['izena'], 4, talde['izena'])
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena'] + ') ---> ERROREA EGON DA TALDEAREN SINGLEA SORTZEAN\n')
		if itemKodea is not None:
			try:
				__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['album'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ') ---> ERROREA EGON DA TALDEAREN DISKAN HONAKO HAU DA GEHITZEAN\n')

	try:
		__add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskaDiskografiaKodea)
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ') ---> ERROREA EGON DA TALDEAREN DISKAN HONEN PARTE DA GEHITZEAN\n')
	
	try:
		__add_statement(site, itemKodea, ag.KODEAK['interpretatzailea'], taldeKodea)
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ') ---> ERROREA EGON DA TALDEAREN INTERPRETATZAILEA GEHITZEAN\n')

	try:
		__add_statement(site, itemKodea, ag.KODEAK['lanaren edo izenaren hizkuntza'], ag.KODEAK['euskara'])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ') ---> ERROREA EGON DA TALDEAREN DISKAN LANAREN EDO IZENAREN HIZKUNTZA GEHITZEAN\n')

	generoak = c.lortuGeneroak(diska['generoa'])
	if generoak is not None:
		for genero in generoak:
			try:
				__add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()],diska['url'], ag.KODEAK['url'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ', '+genero+') ---> ERROREA EGON DA TALDEAREN DISKAN GENEROA GEHITZEAN\n')

	urtea = c.lortuUrteak(diska['urtea'])
	if urtea is not None:
		try:
			__add_dateStatement(site, itemKodea, ag.KODEAK['argitaratze data'], urtea[0], diska['url'], ag.KODEAK['url'])
		except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ', '+urtea[0]+') ---> ERROREA EGON DA TALDEAREN DISKAN URTEA GEHITZEAN\n')

	try:
		__add_badokStatement(site, itemKodea,diska['url'].split('/')[--1])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +diska['izena']  + ') ---> ERROREA EGON DA TALDEAREN DISKAN BADOK GEHITZEAN\n')

	return itemKodea





"""
----------------------TALDEAK SORTUTA EZ DAUDENEAN ERABILTZEKO METODOA: taldeBerriaSortu()-----------------
"""


"""
Metodo honek hiztegi bat jasota talde berria sortuko du oso osorik
(diskografia itema sortuz, horren barruan album eta single-en diskografiaren itemak sortuz 
 eta single eta albumen itemak sortuz)
"""
def taldeBerriaSortu(site, talde):
	itemKodea = __create_item(site,talde['izena'],1,'')
	__add_statement(site,itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['musika talde'])
	urteak= c.lortuUrteak(talde['urtea'])
	if(urteak is not None):
		if(len(urteak)==1):
			__add_dateStatement(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],talde['url'] , ag.KODEAK['url'])
		else:
			__add_dateStatement(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],talde['url'] , ag.KODEAK['url'])
			__add_dateStatement(site, itemKodea, ag.KODEAK['bukaera data'],urteak[1],talde['url'] , ag.KODEAK['url'])
	diskografiaKodea=__taldeBatenDiskografiaSortu(site,talde, itemKodea)
	__add_statement(site, itemKodea, ag.KODEAK['diskografia'], diskografiaKodea)
	herriak = c.lortuHerriak(talde['herria'])
	if herriak is not None:
		__gehitu_herria(site, itemKodea, talde, herriak)
	generoak= c.lortuGeneroak(talde['generoak'])
	if generoak is not None:
		for genero in generoak:
			__add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()], talde['url'] , ag.KODEAK['url'])
	return itemKodea





"""
-------------TALDEA SORTUTA BADAGO ERABILI BEHARKO DEN METODOA: taldeaOsatuKodearekin----------
"""

def taldeaOsatuKodearekin(site,itemKodea, talde):
	badu = False
	try:
		badu = __statementHoriDu(site, itemKodea, ag.KODEAK['honako hau da'])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAK HONAKO HAU DA DUEN AZTERTZEAN\n')

	if not badu:
		try:
			__add_statementTaldeKodearekin(site,itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['musika talde'])
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN HONAKO HAU DA GEHITZEAN\n')
	
	urteak=None
	try:
		urteak= c.lortuUrteak(talde['urtea'])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN URTEAK LORTZEAN\n')

	if(urteak is not None):
		if(len(urteak)==1):
			try:
				__add_dateStatementTaldeKodearekin(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],ag.KODEAK['jaiotze data'], talde['url'] , ag.KODEAK['url'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN SORRERA DATA GEHITZEAN\n')

		else:
			try:
				__add_dateStatementTaldeKodearekin(site, itemKodea, ag.KODEAK['sorrera data'],urteak[0],ag.KODEAK['jaiotze data'],talde['url'] , ag.KODEAK['url'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN SORRERA DATA GEHITZEAN\n')
				
			try:
				__add_dateStatementTaldeKodearekin(site, itemKodea, ag.KODEAK['bukaera data'],urteak[1],ag.KODEAK['deuseztapen data'], talde['url'] , ag.KODEAK['url'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN BUKAERA DATA GEHITZEAN\n')
	try:
		if not __statementHoriDu(site, itemKodea, ag.KODEAK['eraketa lekua']) and not __statementHoriDu(site, itemKodea, ag.KODEAK['jaiolekua']) :
			herriak = c.lortuHerriak(talde['herria'])
			if herriak is not None:
				__gehitu_herria(site, itemKodea, talde, herriak)
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN HERRIA GEHITZEAN\n')
	
	
	baduDiskografia = None
	try:
		baduDiskografia= __statementHoriDu(site, itemKodea, ag.KODEAK['diskografia'])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA DISKOGRAFIA DUEN AZTERTZEAN\n')
	if baduDiskografia is not None:
		if baduDiskografia:
			ag.ERRORE_FITX.write("DISKOGRAFIA DU\n")
			#ag.ERRORE_FITX.write("\n"+dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> OHARRA: TALDEAK BADU DISKOGRAFIA \n')
		else:
			diskografiaKodea=__taldeBatenDiskografiaSortu(site,talde, itemKodea)
			if diskografiaKodea is not None:
				try:
					__add_statement(site, itemKodea, ag.KODEAK['diskografia'], diskografiaKodea)
				except:
					ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN DISKOGRAFIA KODEA GEHITZEAN\n')

	generoak = None
	try:
		generoak= talde['generoak']
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN GENEROAK LORTZEAN\n')

	if generoak is not None:
		for genero in generoak:
			try:
				__add_statementTaldeKodearekin(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()], talde['url'] , ag.KODEAK['url'])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA TALDEAREN GENEROA GEHITZEAN (' +genero +')\n' )
	try:
		__add_badokStatement(site, itemKodea, talde['url'].split("/")[-1])
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + talde['izena'] + ' (' +talde['item_kodea'] + ') ---> ERROREA EGON DA BADOK GEHITZEAN\n')





















'''
def __taldeBatenSingleDiskografia(site,diskografiaKodea, talde, taldeKodea):
	itemKodea=__create_item(site,talde['izena'],5,'')
	__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['singles discography'])
	__add_statement(site, itemKodea, ag.KODEAK['honen parte da'], diskografiaKodea)
	for diska in talde['diskak']:
		if(diska['single']=='True'):
			badagoSingleKodea = __badagoDiska(site, diska, taldeKodea, ag.KODEAK['single'])
			if badagoSingleKodea is None:
				kodeLag = __taldeBatenSingleakSortu(site, diska, taldeKodea, itemKodea, talde)
				__add_statement(site, itemKodea, ag.KODEAK['osatuta'], kodeLag, diska['url'], ag.KODEAK['url'])
			else:
				kodeLag = __taldeBatenSingleakAldatu(site, diska,itemKodea, taldeKodea, talde, badagoSingleKodea)
				__add_statement(site, itemKodea, ag.KODEAK['osatuta'], kodeLag, diska['url'], ag.KODEAK['url'])
			
			
			
			kodeLag= __taldeBatenSingleakSortu(site,diska, itemKodea, taldeKodea, talde)
			__add_statement(site, itemKodea, ag.KODEAK['osatuta'],kodeLag)
	__add_statement(site, itemKodea, ag.KODEAK['honen zerrenda'], ag.KODEAK['single'])
	return itemKodea

def __taldeBatenSingleakAldatu(site, diska, singleDiskografiaKodea, taldeKodea, talde, singleKodea):
    # titulua aldatu eta (albuma) jarri
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo, taldeKodea)
	label= {"eu": diska['izena']+ " (single)", "en": diska['izena'] + " (single)", "es": diska['izena'] +" (single)"}
	item.editLabels(labels=label, summary="Label-ak gehitu")
	description={"en":talde['izena'] +"'s single", "es":"Single de "+ talde['izena'], "eu": talde['izena'] +"(r)en single-a"}
	item.editDescriptions(descriptions=description, summary="Deskribapenak gehitu")
	# honen parte da ... -ren albumak
	__add_statementTaldeKodearekin(site,singleKodea, ag.KODEAK['honen parte da'], singleDiskografiaKodea)
	# genero artistikoa
	generoak = c.lortuGeneroak(diska['generoa'])
	if generoak is not None:
		for genero in generoak:
			try:
				__add_statementTaldeKodearekin(site, singleKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()] ,diska['url'], ag.KODEAK['url'])
			except:
				print(genero + " generoa ez da gehitu " + diska['izena'] + " diskoan.")
	# argitaratze-data
	urtea = c.lortuUrteak(diska['urtea'])
	if urtea is not None:
		__add_dateStatementTaldeKodearekin(site, singleKodea, ag.KODEAK['argitaratze data'], urtea[0], diska['url'], ag.KODEAK['url'])
	__add_statementTaldeKodearekin(site, singleKodea, ag.KODEAK['badok'], diska['url'].split("/")[-2])
	return singleKodea


def __taldeBatenSingleakSortu(site,diska, singleDiskografiaKodea, taldeKodea, talde):
	itemKodea=__create_item(site, diska['izena'],6,talde['izena'])
	__add_statement(site, itemKodea, ag.KODEAK['honako hau da'], ag.KODEAK['single'])
	__add_statement(site, itemKodea, ag.KODEAK['honen parte da'], singleDiskografiaKodea)
	__add_statement(site, itemKodea, ag.KODEAK['interpretatzailea'], taldeKodea, diska['url'] , ag.KODEAK['url'])
	__add_statement(site, itemKodea, ag.KODEAK['lanaren edo izenaren hizkuntza'], ag.KODEAK['euskara'])
	generoak = c.lortuGeneroak(diska['generoa'])
	if generoak is not None:
		for genero in generoak:
			try:
				__add_statement(site, itemKodea, ag.KODEAK['genero artistikoa'], ag.GENEROAK[genero.lower()],diska['url'], ag.KODEAK['url'])
			except:
				print(genero + " generoa ez da gehitu " + diska['izena'] + " diskoan.")
	urtea= c.lortuUrteak(diska['urtea'])
	if urtea is not None:
		__add_dateStatement(site, itemKodea, ag.KODEAK['argitaratze data'],urtea[0], diska['url'] , ag.KODEAK['url'])
	return itemKodea
'''