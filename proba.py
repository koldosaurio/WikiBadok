from urllib.request import urlopen
from bs4 import BeautifulSoup


def izenak_lortu():
	url = "https://www.badok.eus/euskal-musikak/"
	html = urlopen(url).read().decode("utf-8")
	izenLista=[]
	
	soup =  BeautifulSoup(html, 'html.parser')
	sections = soup.body('section')
	for section in sections:
		if section['class'][0] == 'letra_bakoitza':
			for a in section('a'):
				izenLista.append(a.string)
	return izenLista
