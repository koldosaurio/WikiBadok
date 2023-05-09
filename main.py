from funtzioak import datuak_lortu
import csv
import aldagaiGlobalak as ag
from datetime import datetime as dt


datuak = datuak_lortu()
print('\nDatuak lortuta\n')

file=open('taldeak.csv', 'w', newline='')
filedisk= open('diskak.csv', 'w', newline='')
filesong = open('kantak.csv', 'w', newline='')

writer = csv.writer(file)
writerdisk = csv.writer(filedisk)
writersong = csv.writer(filesong)

for taldea in datuak:
	try:
		writer.writerow([taldea['id'], taldea['izena'],taldea['biografia'], taldea['urtea'], taldea['herria'], taldea['generoak'], taldea['url']])
		for diska in taldea['diskak']:
			try:
				writerdisk.writerow([diska['id'], diska['izena'], diska['url'],diska['generoa'], diska['single'], taldea['id']])
				try:
					for kanta in diska['kantak']:
						writersong.writerow([kanta, diska['id']])
				except:
					ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + diska['izena'] + ' taldearen kantak gehitzerakoan arazoak \n')
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + taldea['izena'] + ' taldearen diskak gehitzerakoan arazoak \n')
	except:
		ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + taldea['izena'] + ' taldea gehitzerakoan arazoak izan dira \n')
		
filedisk.close()
filesong.close()
file.close()