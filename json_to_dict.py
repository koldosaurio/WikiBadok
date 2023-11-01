import json
import pywikibot
import csvreader as ir


def __getLabel(site, itemCode):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	item_dict = item.get()
	label = ''
	try:
		label = item_dict['labels']['eu']
	except:
		label = None
	return label

def __lortu_musikastenID(site):
	with open("./musikastenID/musikastenID.json", 'r') as mID:
		hizt = json.load(mID)
		emaitza = {}
		for elem in hizt:
			url = elem['item'].split('/')
			itemCode = url[-1]
			izena = __getLabel(site, itemCode)
			if izena != None:
				emaitza[izena.lower().replace(" ", "")] = itemCode
		return(emaitza)
	
def musikasten_vs_badok(taldeak, site):
	emaitza = __lortu_musikastenID(site)
	bueltatzeko=[]
	for taldea in taldeak:
		if taldea['izena'].lower().replace(" ", "") in emaitza.keys():
			taldea['item_kodea']= emaitza[taldea['izena'].lower().replace(" ", "")]
			bueltatzeko.append(taldea)
	return bueltatzeko



