# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:43:50 2023

@author: Koldo
"""
import csv


def __irakurri_taldeak(file1):
	taldeak=[]
	taldereader=csv.reader(open(file1, 'r'), delimiter=',')
	for row in taldereader:
		
		talde={}
		talde['id'], talde['izena'], talde['biografia'],talde['urtea'], talde['herria'], talde['url']=row[0], row[1], row[2], row[3], row[4], row[6]
		talde['generoak']=[]
		talde['diskak']=[]
		for kar in row[5].split('\''):
			if kar != '[' and kar != ']' and kar != '\'' and kar!=', ':
				talde['generoak'].append(kar.replace(',', ''))
		taldeak.append(talde)
		
	return taldeak

def __irakurri_diskak(file1, file2):
	diskakreader = csv.reader(open(file2, 'r'), delimiter=",")
	taldeak = __irakurri_taldeak(file1)
	taldea=0
	taldeaid=1
	
	for row in diskakreader:
		diska ={}
		diska['id'], diska['izena'], diska['url'], diska['generoa'], diska['single']=row[0], row[1], row[2], row[3], row[4]

		if taldeaid!=int(row[5]):
			taldeaid=int(row[5])
			while int(taldeak[taldea]['id'])<taldeaid:
				taldea+=1
		if int(taldeak[taldea]['id'])==taldeaid:
			taldeak[taldea]['diskak'].append(diska)
	return taldeak

def lortu_datuak(a, b, c):
	"""
	

	Parameters
	----------
	a : string
		taldeak dauden .csv fitxategia
	b : string
		diskak dauden .csv fitxategia
	c : string
		kantak dauden .csv fitxategia

	Returns
	-------
	list
		talde zerrenda bat bueltatzen du bere kantekin batera

	"""
	return __irakurri_diskak(a, b)



def lortuGeneroak(generoak):
	emaitza = []
	if(generoak==''):
		return None
	elif generoak[0]=='"':
		chars='" '
		emaitza= generoak.translate(str.maketrans('', '', chars))
		emaitza = emaitza.split(',')
		return emaitza
	else:
		emaitza.append(generoak)
		return emaitza

def lortuUrteak(urteak):
	
	if urteak != '':
		urteLista=[]
		emaitza= urteak.split('-')
		print(emaitza)
		for elem in emaitza:
			urteLista.append(int(elem))
		return urteLista
	else:
		return None
