# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:43:50 2023

@author: Koldo
"""
import csv
import re


def __irakurri_taldeak(file1):
	taldeak=[]
	taldereader=csv.reader(file1, delimiter=',')
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
	diskakreader = csv.reader(file2, delimiter=",")
	taldeak = __irakurri_taldeak(file1)
	taldea=0
	taldeaid=1
	
	for row in diskakreader:
		diska ={}
		diska['id'], diska['izena'], diska['url'], diska['generoa'], diska['single'], diska['urtea']=row[0], row[1], row[2], row[3], row[4], row[5]

		if taldeaid!=int(row[6]):
			taldeaid=int(row[6])
			while int(taldeak[taldea]['id'])<taldeaid:
				taldea+=1
		if int(taldeak[taldea]['id'])==taldeaid:
			taldeak[taldea]['diskak'].append(diska)
	return taldeak

def lortu_datuak(a = './datuak/taldeak.csv', b = './datuak/diskak.csv', c = './datuak/kantak.csv'):
	"""
	
	!!Adi!!
	---------
	WikiBadok karpetatik kanpo baldin bazabiltza komenigarria da a eta b parametroei balioa pasatzea 
	zure karpetarekiko behar dituzun fitxategien ruta erlatiboak erabiliz.

	Parameters
	----------
	a : string
		taldeak dauden .csv fitxategia
		defektuz ./datuak/taldeak.csv fitxategia irekitzen du
	b : string
		diskak dauden .csv fitxategia
		defektuz ./datuak/diskak.csv fitxategia irekitzen du
	c : string
		kantak dauden .csv fitxategia (open eginda jada, read moduan irekita)
		defektuz ./datuak/kantak.csv fitxategia irekitzen du

	Returns
	-------
	list
		talde zerrenda bat bueltatzen du bere kantekin batera
		
	

	"""
	return __irakurri_diskak(open(a, 'r'), open(b, 'r'))



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
		for elem in emaitza:
			urteLista.append(int(elem))
		return urteLista
	else:
		return None


def lortuHerriak(herriak):

	if(herriak==''):
		return None
	else:
		cadena_sin_parentesis = re.sub(r'\([^()]*\)', '', herriak)
		resultado = cadena_sin_parentesis.split(',')
		resultado = [elemento.strip() for elemento in resultado]
		return resultado
