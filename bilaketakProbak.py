# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:50:12 2023

@author: anepa
"""
import pywikibot
import bilaketakFuntzioak
import csv

site = pywikibot.Site("eu", "wikipedia")
taldeak=[]
with open('D:/SourceTree/WikiData/taldeak.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        taldeIzena = row[1]
        taldeak.append(taldeIzena)
        
    with open('./ezDaudenTaldeak.csv', 'w', newline = '') as ezDaude:
            writerEzDaude = csv.writer(ezDaude)
            with open('./badaudenTaldeak.csv', 'w', newline = '') as badaude:
                writerBadaude = csv.writer(badaude)
                
                with open('./taldeHutsak.csv', 'w', newline = '') as hutsak:
                        writerHutsak = csv.writer(hutsak)
                        
                        with open('./taldeArraroak.csv', 'w', newline = '') as arraro:
                                writerArraro = csv.writer(arraro)
                                
                                for taldeIzena in taldeak:
                                    em = bilaketakFuntzioak.wikidatanDago(site, taldeIzena)
                                    if(em != []):
                                        if(em[2] == None): writerHutsak.writerow(em)
                                        elif('musikari' in em[2] or
                                           'abeslari' in em[2] or
                                           'talde' in em[2]):
                                            writerBadaude.writerow(em)
                                        else: writerArraro.writerow(em)
                                    else: writerEzDaude.writerow([taldeIzena])
                                arraro.close()
                        hutsak.close()        
                badaude.close()
            ezDaude.close()
    file.close()
