import funtzioak
import csv
import aldagaiGlobalak as ag


datuak=funtzioak.datuak_lortu()
print('\nDatuak lortuta\n')
#print(proba.izenak_lortu())
with open('taldeak.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for i in range(len(datuak)):
		try:
			for diska in datuak[i]['diskak']:
				writer.writerow([datuak[i]['izena'], diska['izena'], datuak[i]['url']])
		except:
			print(datuak[i]['izena'] + ' taldearen diskak: \n' + datuak[i]['diskak'])
#print(funtzioak.datuak_lortu())