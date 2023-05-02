from urllib.request import urlopen
from bs4 import BeautifulSoup
import aldagaiGlobalak as ag
from datetime import datetime as dt


def __izenak_lortu():
	"""
	badokeko lehen orrialdeko musikarien zerrenda bat sortzen du
	aldagai globaletako hasiera_url aldagaia erabiliz

	Returns
	-------
	izenLista : List
		talde bakoitzagatik dictionary bat izango du non izena eta url key-ak izango dituen
		

	"""
	
	url = ag.hasiera_url
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	izenLista=[]
	for section in soup.body(attrs={'class', 'letra_bakoitza'}):
		for a in section('a'):
			izenLista.append({'id': ag.TALDE_ID,'izena': a.string, 'url': a['href'].replace(' ','%20')})
			ag.TALDE_ID+=1
	return izenLista

def __kantak_lortu(soup):
	"""
	diska bakoitzeko kantak lortuko ditu eta lista bat eta boolean bat itzuliko ditu

	Parameters
	----------
	soup : beautyfulsoup soup
		Beatutyfulsoup() funtzioak bueltatzen duen datu mota

	Returns
	-------
	kantak : List
		Diskoak dituen kantuen izenak
	single: boolean
		True diskoak kanta bakarra badauka False bestela

	"""
	kantak=[]
	for div in soup.body.find_all(attrs={'class': 'abesti_lista_abesti'}):
		kantak.append(div.contents[0])
	return (kantak, len(kantak)==1)

#TODO
# control aldagaiaren erabilera kendu eta funtzioa ondo jarri
def __diskaren_datuak_lortu(soup):
	"""
	Eskuragai dauden diskaren atributuak bueltatuko dituen funtzioa 

	Parameters
	----------
	soup : beautyfulsoup soup
		Beatutyfulsoup() funtzioak bueltatzen duen datu mota

	Returns
	-------
	TODO : TODO
		TODO

	"""
	generoa=''
	control=False
	for item in soup.body.find(attrs={'class': 'taldea_diska'})('p'):
		informazioa=item.string
		if control:
			generoa=informazioa
			control=False
		if 'GENEROA' == informazioa:
			control=True
	return generoa

def __diskaren_informazioa_lortu(url, datuak):
	"""
	Diskaren informazio guztia datuak dictionary-an gordeko dituen funtzioa, interfaze antzeko bat da

	Parameters
	----------
	url : string
		Bilatu nahi den diskaren url-a badok-eko web orrialdean
	datuak : dictionary
		informazioa gordeko den datu egitura

	Returns
	-------
	datuak : dictionary
		diskaren informazioarekin beteriko datu egitura

	"""
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	datuak['kantak'], datuak['single']=__kantak_lortu(soup)
	datuak['generoa']=__diskaren_datuak_lortu(soup)
	return datuak

def __taldearen_diskoak_lortu(soup):
	"""
	

	Parameters
	----------
	soup : beautyfulsoup soup
		Beatutyfulsoup() funtzioak bueltatzen duen datu mota

	Returns
	-------
	diskak : List
		Taldearen diska bakoitzeko dictionary bat izango duen datu egitura

	"""
	diskak = []
	for div in soup.body.find(id='diskografia').find_all(attrs={'class': 'tit'}):
		diska={}
		etiketa= div.a
		diska['id']=ag.DISKA_ID
		ag.DISKA_ID+=1
		diska['izena'] =etiketa.string
		diska['url'] = etiketa['href'].replace(' ', '%20')
		__diskaren_informazioa_lortu(diska['url'], diska)
		diskak.append(diska)
	return diskak

def __taldearen_biografia_lortu(soup):
	"""
	

	Parameters
	----------
	soup : beautyfulsoup soup
		Beatutyfulsoup() funtzioak bueltatzen duen datu mota

	Returns
	-------
	biografia : string
		Taldeak web orrian eskatzen duen biografia txikitxoa string formatuan
	"""
	biografia=''
	if soup.body.find(attrs={'class', 'taldeintro_more'}).p :
		biografia = soup.body.find(attrs={'class', 'taldeintro_more'}).p.string
	return biografia
	
def __taldearen_oinarrizko_datuak_lortu(soup):
	"""
	Taldearen sorkuntza urtea, sorkuntza herria eta generoa(k) itzuliko dituen metodoa

	Parameters
	----------
	soup : beautyfulsoup soup
		Beatutyfulsoup() funtzioak bueltatzen duen datu mota

	Returns
	-------
	urtea : string
		Taldearen sorkuntza urtea edota hasiera eta amaiera urteak
	herria : string
		taldearen sorkuntza herria
	generoak : list
		taldearen generoak lista batetan edukita

	"""
	urtea=''
	herria=''
	generoak=[]
	for i in soup.body.find(attrs={'class': 'perfila'}).ul('li'):
		edukiak=i.contents
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
				try: 
					generoak=edukiak[1].split(' ')
				except:
					print(edukiak)
					ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + ' --> Generoarekin zerbait gertatu da\n')
	
	return (urtea, herria, generoak)

def __taldearen_informazioa_lortu(url, datuak):
	"""
	taldearen informazioa guztia lortzeko erabili beharreko metodoei dei egiten dien metodoa
	bitartekari antzeko bat da

	Parameters
	----------
	url : string
		datuak lortu nahi diren taldearen badok-eko url-a
	datuak : dictionary
		lortuko diren datuak gordeko diren datu egitura

	Returns
	-------
	datuak : dictionary
		jasotako datu egitura berbera lorturiko datuekin beteta

	"""
	html = urlopen(url).read().decode("utf-8")
	soup =  BeautifulSoup(html, 'html.parser')
	datuak['diskak']=__taldearen_diskoak_lortu(soup)
	datuak['biografia']=__taldearen_biografia_lortu(soup)
	datuak['urtea'], datuak['herria'], datuak['generoak']= __taldearen_oinarrizko_datuak_lortu(soup)
	return datuak

def datuak_lortu():
	"""
	Datu guztiak lortzeko erabiltzen den funtzioa

	Returns
	-------
	datuak : List
		Listako posizio bakoitzak talde baten datuak dituen dictionary bati dagokio

	"""
	datuak = __izenak_lortu()
	
	#hemen erabakitzen da zenbat elementu hartu behar dituen ta zeintzuk
	for i in range(len(datuak)):
		#TODO filtro bat da izen bat topatzeko
		# if datuak[i]['izena'].lower() in ag.IZEN_FILTROA:
			try:
				datuak[i] =__taldearen_informazioa_lortu(datuak[i]['url'], datuak[i])
			except:
				ag.ERRORE_FITX.write(dt.now().strftime("%H:%M:%S") + ' --> Arazoak ondoko taldearen informazioa lortzerakoan: ' + datuak[i]['izena'] + '\n')
	return datuak
