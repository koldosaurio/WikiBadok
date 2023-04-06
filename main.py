import funtzioak
import csv
import aldagaiGlobalak as ag


datuak=funtzioak.datuak_lortu()
#print(proba.izenak_lortu())
with open('taldeak.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for i in range(ag.ZENBAT_IZEN):
		for diska in datuak[i]['diskak']:
			writer.writerow([datuak[i]['izena'], diska['izena'], datuak[i]['url']])
#print(funtzioak.datuak_lortu())