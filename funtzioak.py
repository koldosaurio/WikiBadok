from urllib.request import urlopen
from bs4 import BeautifulSoup
import aldagaiGlobalak as ag


def izenak_lortu():
	url = "https://www.badok.eus/euskal-musikak/"
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	izenLista=[]
	for section in soup.body(attrs={'class', 'letra_bakoitza'}):
		for a in section('a'):
			izenLista.append({'izena': a.string, 'url': a['href'].replace(' ','%20')})
	return izenLista

def kantak_lortu(soup):
	kantak=[]
	for div in soup.body.find_all(attrs={'class': 'abesti_lista_abesti'}):
		kantak.append(div.contents[0])
	return (kantak, len(kantak)==1)

#TODO
# control aldagaiaren erabilera kendu eta funtzioa ondo jarri
def diskaren_datuak_lortu(soup):
	generoa=''
	control=False
	for item in soup.body.find(attrs={'class': 'taldea_diska'})('p'):
		informazioa=item.string
		#print(str(item) + '\n\n\n')
		if control:
			generoa=informazioa
			control=False
		if 'GENEROA' == informazioa:
			control=True
	return generoa

def diskaren_informazioa_lortu(url, datuak):
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	datuak['kantak'], datuak['single']=kantak_lortu(soup)
	datuak['generoa']=diskaren_datuak_lortu(soup)
	return datuak

def taldearen_diskoak_lortu(soup):
	diskak = []
	for div in soup.body.find(id='diskografia').find_all(attrs={'class': 'tit'}):
		diska={}
		etiketa= div.a
		diska['izena'] =etiketa.string
		diska['url'] = etiketa['href'].replace(' ', '%20')
		diskaren_informazioa_lortu(diska['url'], diska)
		diskak.append(diska)
	return diskak

def taldearen_biografia_lortu(soup):
	biografia=''
	if soup.body.find(attrs={'class', 'taldeintro_more'}).p :
		biografia = soup.body.find(attrs={'class', 'taldeintro_more'}).p.string
	return biografia
	
def taldearen_oinarrizko_datuak_lortu(soup):
	urtea=''
	herria=''
	generoak=[]
	for i in soup.body.find(attrs={'class': 'perfila'}).ul('li'):
		edukiak=i.contents
		print(edukiak)
		try:
			if '-' not in edukiak[0]:
				int(edukiak[0])
				urtea=edukiak[0]
			else:
				int(edukiak[0].split('-')[0])
				urtea=edukiak[0]
		except:
			if '<strong>Herria:</strong>' in edukiak[0]:
				herria=edukiak[1]
			else:
				generoak=edukiak[1].split(' ')
	
	return (urtea, herria, generoak)

def taldearen_informazioa_lortu(url, datuak):
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	datuak['diskak']=taldearen_diskoak_lortu(soup)
	datuak['biografia']=taldearen_biografia_lortu(soup)
	datuak['urtea'], datuak['herria'], datuak['generoak']= taldearen_oinarrizko_datuak_lortu(soup)
	return datuak

def datuak_lortu():
	datuak=izenak_lortu()
	#hemen erabakitzen da zenbat elementu hartu behar dituen ta zeintzuk
	for i in range(len(datuak)):
		#TODO filtro bat da izen bat topatzeko
		#if datuak[i]['izena'] in ag.IZEN_FILTROA:
		try:
			datuak[i] =taldearen_informazioa_lortu(datuak[i]['url'], datuak[i])
		except:
			print('talde arazoa: '+datuak[i]['izena'])
	return datuak
