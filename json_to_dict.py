import json
import pywikibot


def getLabel(site, itemCode):
	repo = site.data_repository()
	item = pywikibot.ItemPage(repo,itemCode)
	item_dict = item.get()
	label = ''
	try:
		label = item_dict['labels']['eu']
	except:
		print(itemCode, " kodeak ez du labelik")
	return label

def lortu_musikastenID(site):
	with open("./musikastenID/musikastenID.json", 'r') as mID:
		hizt = json.load(mID)
		emaitza = {}
		for elem in hizt:
			url = elem['item'].split('/')
			itemCode = url[4]
			izena = getLabel(site, itemCode)
			emaitza[itemCode] = izena
		return(emaitza)

