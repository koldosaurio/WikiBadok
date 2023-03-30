import funtzioak
import csv


datuak=funtzioak.datuak_lortu()
#print(proba.izenak_lortu())
with open('taldeak.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for i in range(50):
		for diska in datuak[i]['diskak']:
			writer.writerow([datuak[i]['izena'], diska, datuak[i]['url']])
