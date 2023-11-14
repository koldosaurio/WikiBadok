# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:37:53 2023

@author: Koldo
"""

hasiera_url="https://www.badok.eus/euskal-musikak/"
ZENBAT_IZEN=10
IZEN_FILTROA=['hesian', 'niña coyote eta chico tornado']
TALDE_ID=1
DISKA_ID=1
ERRORE_FITX=open(r".\logs\erroreak.log", "a")

AMAIERAK1=['a','e','i','o','u','r','w', '2', '3', '4', '6', '7', '8', '9']
AMAIERAK2=['11', '20','40', '60', '80']

KODEAK={
'honako hau da':'P31',
'diskografia':'P358',
'musika talde':'Q215380',
'gizaki':'Q5',
'sorrera data':'P571',
'jaiotze data': 'P569',
'bukaera data':'P582',
'deuseztapen data':'P576',
'eraketa lekua':'P740',
'jaiolekua':'P19',
'genero artistikoa':'P136',
'osatuta':'P527',   #taldeetako kideak zeintzuk diren esateko
'badok':'P9558',

'wikimedia artist discography':'Q104635718',
'elementuaren zerrenda':'P2354',

'wikimedia albums discography':'Q59191021',
'honen parte da':'P361',
'honen zerrenda':'P360',
'album':'Q482994',

'izenburua':'P1476',
'interpretatzailea':'P175',
'diskoetxea':'P264',
'lanaren edo izenaren hizkuntza':'P407',
'euskara':'Q8752',
'argitaratze data':'P577',
'abesti zerrenda':'P658',

'musika lan':'Q105543609',
'single':'Q134556',

'singles discography':'Q59248059',

'url':'P854'
}

GENEROAK={
'afrobeata':'Q388296',
'bertsoa':'Q1661',
'black metala':'Q132438',
'bluesa':'Q9759',
'countrya':'Q83440',
'cumbia':'Q723418',
'dance':'Q851213',
'elektro-folka':'Q107486984',
'elektro-swinga':'Q602561',
'elektronikoa':'Q9778',
'esperimentala':'Q1640319',
'flamenkoa':'Q9764',
'folk-popa':'Q11700058',
'folk-rocka':'Q186472',
'folka':'Q43343',
'funka':'Q164444',
'hard-rocka':'Q83270',
'hardcorea':'Q11974316',
'herri kanta':'Q235858',
'indie-folka':'Q1317816',
'industriala':'Q487965',
'jazz-rocka':'Q944465',
'jazza':'Q8341',
'kantautorea':'Q488205',
'klasikoa':'Q9730',
'metala':'Q38848',
'noise-rocka':'Q181861',
'plaza':'Q118123408',
'pop-rocka':'Q484641',
'popa':'Q37073',
'post-folka':'Q118123304',
'post-hardcorea':'Q377910',
'post-punka':'Q598929',
'post-rocka':'Q209137',
'progresiboa':'Q7248857',
'punk-oi!':'Q274401',
'punk-rocka':'Q3071',
'punka':'Q3071',
'rap-metala':'Q856872',
'rapa':'Q6010',
'reggaea':'Q9794',
'reggaetona':'Q202930',
'rock&rolla':'Q7749',
'rocka':'Q11399',
'runba':'Q388475',
'salsa':'Q208239',
'ska':'Q54365',
'ska-rocka':'Q3486097',
'soinu-banda':'Q217199',
'soula':'Q131272',
'stonerra':'Q617240',
'thrasha':'Q483352',
'triki-popa':'QQ118123362',
'trikitia':'Q29252685'
}


#SALBUESPENAK:
#	URRETXU-ZUMARRAGA = URRETXU+ZUMARRAGA
#	AZPEITIA-ZARAUTZ = AZPEITIA + ZARAUTZ
#	BESKOITZE-BILBO = BESKOITZE + BILBO
#	IRUÑEA-DONOSTI-BILBO
#	Oiartzun -Donostia
#	Ziburu-Donibane Lohizune
#	'Uztaritze -Tolosa'
#	'Donibane-Ziburu'
HERRIAK={
'Andoain':'Q1598976',
'Barakaldo':'Q487801',
'Bilbo':'Q37166526',
'Zarautz':'Q147774',
'Herrialde Katalanak':'Q234963',
'Urruña':'Q672401',
'Elgoibar':'Q24001637',
'Ondarroa':'Q595283',
'Soraluze':'Q118153808',
'Gasteiz':'Q53155438',
'Azkoitia':'Q793934',
'Balmaseda':'Q4480',
'Hondarribia':'Q492312',
'Bermeo':'Q695444',
'Bergara':'Q1382252',
'Tolosa':'Q497801',
'Donostia':'Q57669050',
'Iruñea':'Q10282',
'Getxo':'Q492420',
'Barañain':'Q768691',
'Bera':'Q818675',
'Laudio':'Q3381376',
'Basauri':'Q765496',
'Galdakao':'Q1227388',
'Legazpi':'Q1113716',
'Armendaritze':'Q548220',
'Eibar':'Q496567',
'Zugarramurdi':'Q1643583',
'Mendillorri':'Q3015620',
'Hernani':'Q1441329',
'Gernika':'Q189848',
'Zornotza':'Q95630408',
'Irurtzun':'Q674117',
'Miarritze':'Q132790',
'Oiartzun':'Q911092',
'Urretxu-Zumarraga':'None',
'Hazparne':'Q197150',
'Baiona':'Q748867',
'Irunberri':'Q584132',
'Altzürükü':'Q274207',
'Donapaleu':'Q266826',
'Zubieta':'Q1643571',
'Gipuzkoa':'Q95010',
'Usurbil':'Q1633909',
'Irun':'Q200201',
'Astigarraga':'Q1639355',
'Pasaia':'Q847127',
'Durango':'Q79918',
'Leioa':'Q530302',
'Mutriku':'Q1618305',
'Ordizia':'Q672483',
'Arrasate':'Q491922',
'Arrangoitze':'Q197339',
'Zestoa':'Q1618393',
'Oñati':'Q496588',
'Elorrio':'Q1242382',
'Busturia':'Q1242317',
'Bizkaia':'Q95614221',
'Iruñerria':'Q2598724',
'Muskiz':'Q607474',
'Errenteria':'Q681893',
'Lasarte-Oria':'Q932766',
'Beasain':'Q847130',
'Bolibar':'Q95614248',
'Nafarroa':'Q6557387',
'Bartzelona':'Q29976333',
'Angelu':'Q27909226',
'Arbizu':'Q1645754',
'Mungia':'Q1228780',
'Gernika-Lumo':'Q24016799',
'Aduna':'Q576753',
'Orio':'Q1649616',
'Lekunberri':'Q1773037',
'Ataun':'Q1619442',
'Zaldibia':'Q1618289',
'Bordele':'Q1479',
'Arrigorriaga':'Q283607',
'Zumaia':'Q229659',
'Villabona':'Q672876',
'Ainhize-Monjolose':'Q839563',
'Ziburu':'Q235208',
'Lazkao':'Q932872',
'Abadiño':'Q744893',
'Santurtzi':'Q917886',
'Doneztebe':'Q107207639',
'Mallabia':'Q1227994',
'Ermua':'Q1242400',
'Maruri-Jatabe':'Q678721',
'Azpeitia':'Q180611',
'Igorre':'Q779046',
'Lezo':'Q1649625',
'Donibane Garazi':'Q270294',
'Lekeitio':'Q1227965',
'Hendaia':'Q191754',
'Agurain':'Q117244943',
'Irulegi':'Q66134753',
'Portugalete':'Q548441',
'Itsasu':'Q683474',
'Lesaka':'Q1647457',
'Ereñotzu':'Q12257018',
'Urdiñarbe':'Q840674',
'Bakio':'Q804466',
'Arabako Errioxa':'Q282024',
'Aretxabaleta':'Q935603',
'Ugao':'Q113481768',
'Meñaka':'Q647357',
'Kanbo':'Q26438275',
'Algorta':'Q29353',
'Baigorri':'Q48008135',
'Azpeitia-Zarautz':'None',
'Allotz':'Q108804355',
'Altzaga':'Q1639435',
'Arratia':'Q37095183',
'Artea':'Q1242330',
'Aia':'Q1631163',
'Beskoitze -Bilbo':'None',
'Sestao':'Q909707',
'Nafarroa Beherea':'Q638503',
'Berriz':'Q747628',
'Donibane Lohizune':'Q232135',
'Ea':'Q1228081',
'Zizur':'Q1228466',
'Gares':'Q3098284',
'Amurrio':'Q481760',
'Luhuso':'Q842624',
'Uharte':'Q52717504',
'Oztibarre':'Q3092103',
'Tafalla':'Q820224',
'Durangaldea':'Q615017',
'Zeanuri':'Q169332',
'Iruñea-Donostia-Bilbo':'None',
'Tarragona':'Q15088',
'Uribe Kosta':'Q3552303',
'Markina-Xemein':'Q604810',
'Lapurdi':'Q671023',
'Behe Nafarroa':'Q638503',
'Urduña':'Q225662',
'Urizahar':'Q1452675',
'Enkarterri':'Q582166',
'Urretxu':'Q904269',
'Caracas':'Q1533',
'Senpere':'Q95629643',
'Trapagaran':'Q8343805',
'Aramaio':'Q976743',
'Zizurkil':'Q1618316',
'Lizarra':'Q108136582',
'Laukiz':'Q1246777',
'Zumarraga':'Q844508',
'Elizondo':'Q3051309',
'Errezil':'Q964114',
'Aldude':'Q106878106',
'Larrabetzu':'Q784127',
'Arrokiaga':'Q840691',
'Gabadi':'Q61385614',
'Muxika':'Q664870',
'Anoeta':'Q1640537',
'Etxarri-Aranatz':'Q29975427',
'Oiartzun -Donostia':'None',
'Bortziriak':'Q2606207',
'Usansolo':'Q9092080',
'Lezama':'Q946068',
'Baztan':'Q641755',
'Leitza':'Q1648056',
'Lizartza':'Q1633857',
'Antzuola':'Q1625886',
'Biana':'Q18443625',
'Bastida':'Q36884902',
'Muskildi':'Q535638',
'Urnieta':'Q1633844',
'Etxebarri':'Q1228107',
'Larraintzar':'Q3217987',
'Lemoa':'Q1227196',
'Ziburu-Donibane Lohizune':'None',
'Zorrotza':'Q3497419',
'Barkoxe':'Q839436',
'Arrosa':'Q20491623',
'Altzo':'Q1639371',
'Ezkerraldea':'Q3111505',
'Landibarre':'Q324227',
'Mendaro':'Q629193',
'Burlata':'Q24012487',
'Behorlegi':'Q317341',
'Malerreka':'Q2606221',
'Idiazabal':'Q1619118',
'Gotaine-Iribarne':'Q178701',
'Uztaritze -Tolosa':'None',
'Uztaritze':'Q269874',
'Hego Uribe':'Q3129383',
'Donibane Lohitzune':'Q232135',
'Donibane-Loitzune':'Q232135',
'Amsterdam':'Q727',
'Atarrabia':'Q95077577',
'Lizarraldea':'Q2659030',
'Dima':'Q663530',
'Getaria':'Q849330',
'Oronoz':'Q37274420',
'Beskoitze':'Q675447',
'Azkaine':'Q838300',
'Madril':'Q37467619',
'Ezpeleta':'Q36891962',
'Maule':'Q751559',
'Berlin':'Q64',
'Amaiur':'Q452571',
'Larraga':'Q1647936',
'Legorreta':'Q1639412',
'Getari':'Q672766',
'Antsoain':'Q110605210',
'Sara':'Q833345',
'Olazti':'Q12265097',
'Altsasu':'Q100257363',
'Ibarrangelu':'Q1227981',
'Elantxobe':'Q735451',
'Anhauze':'Q197023',
'Sakana':'Q2476592',
'Zuraide':'Q645206',
'Urepele':'Q839971',
'Lekaroz':'Q3229254',
'Sopuerta':'Q1228749',
'Iraizotz':'Q3154258',
'Mundaka':'Q786126',
'Donibane-Ziburu':'None'
}