# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:43:50 2023

@author: Koldo
"""
import csv

file1=''
file2=''
file3=''

def __irakurri_taldeak(file1):
	taldeak=[]
	taldereader=csv.reader(open(file1, 'r'), delimiter=',')
	for row in taldereader:
		
		talde={}
		talde['id'], talde['izena'], talde['biografia'],talde['urtea'], talde['herria'], talde['url']=row[0], row[1], row[2], row[3], row[4], row[6]
		talde['generoak']=[]
		talde['diskak']=[]
		for kar in row[5].split('\''):
			if kar != '[' and kar != ']' and kar != '\'':
				talde['generoak'].append(kar)
		taldeak.append(talde)
		
	return taldeak

#TODO k pereza, etxata okurritzen, beste baterako
def __irakurri_diskak(file1, file2):
	diskakreader = csv.reader(open(file2, 'r'), delimiter=",")
	taldeak = __irakurri_taldeak(file1)
	taldea=1
	
	for row in diskakreader:
		diska ={}
		diska['id'], diska['izena'], diska['url'], diska['generoa'], diska['single']=row[0], row[1], row[2], row[3], row[4]

		if int(taldeak[1]['id'])<int(row[5]):
			taldea+=1
		try:
			taldeak[taldea-1]['diskak'].append(diska)
		except:
			print(taldea)
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