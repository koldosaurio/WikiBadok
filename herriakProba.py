# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:43:29 2023

@author: anepa
"""

import bilaketakFuntzioak as bf
import csvreader as c
import csv


#fileHerri=open("./herriak/herriakKodigoekin.csv", 'w', newline='')

#writerHerri = csv.writer(fileHerri)

"""
with open("./herriak/herriakSinplifikatuta.csv", 'r') as herri_csv:
	herrireader=csv.reader(herri_csv)
	for row in herrireader:
		emaitza = bf.wikidatanDago(row[0])
		print(row[0] + ': ' + str(emaitza) )
		writerHerri.writerow([f"'{row[0]}' : '{emaitza}'"])
"""
with open("./herriak/herriakKodigoekin.csv", 'r') as herri_csv:
	herrireader=csv.reader(herri_csv)
	hiztegia = {}
	for row in herrireader:
		print(row)
		zatiak = row[0].split(':')
		klabea = zatiak[0]
		balioa = zatiak[1]
		balioa = balioa[1:]
		hiztegia[klabea]= balioa
	for key, value in hiztegia.items():
		print(f"'{key}':'{value}'")

#bf.herriSinplifikatuakLortu()