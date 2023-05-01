import funtzioak
import csv
import aldagaiGlobalak as ag
from datetime import datetime as dt


datuak=funtzioak.datuak_lortu()
print('\nDatuak lortuta\n')
with open('taldeak.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for taldea in datuak:
		writer.writerow([taldea['id'], taldea['izena'], taldea['url']])
		try:
			for diska in taldea['diskak']:
				with open('diskak.csv', 'w', newline='') as filedisk:
					writerdisk = csv.writer(filedisk)
					writerdisk.writerow(diska['id'], diska['izena'], diska['url'],diska['generoa'], diska['single'], taldea['id'])
					for kanta in diska['kantak']:
						with open('kantak.csv', 'w', newline='') as filesong:
							writersong = csv.writer(filesong)
							writersong.writerow(kanta, diska['id'])
						filesong.close()
				filedisk.close()
		except:
			ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + taldea['izena'] + ' taldearen diskak gehitzerakoan arazoak \n')
file.close()