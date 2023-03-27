from urllib.request import urlopen
from bs4 import BeautifulSoup


def izenak_lortu():
	url = "https://www.badok.eus/euskal-musikak/"
	html = urlopen(url).read().decode("utf-8")
	izenLista=[]
	
	soup =  BeautifulSoup(html, 'html.parser')
	for section in soup.body('section'):
		if section['class'][0] == 'letra_bakoitza':
			for a in section('a'):
				izenLista.append({'izena': a.string, 'url': a['href']})
	return izenLista

def taldearen_diskoak_lortu(url):
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	diskak = []
	for div in soup.body.find(id='diskografia').find_all(attrs={'class': 'row'}):
		if 'konpartitu' not in div.attrs['class']:
			diskak.append(div.find_all(attrs={'class':'col-md-4'})[1].a.string)
	return diskak