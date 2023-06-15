# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:50:12 2023

@author: anepa
"""
import csvreader
import bilaketakFuntzioak
import csv


print(bilaketakFuntzioak.wikidatanDago('Iheskide'))
# datuak = csvreader.lortu_datuak('./taldeak.csv','./diskak.csv','./kantak.csv');
# fileEz=open('euskarazkoLabelikEz.csv', 'w', newline='')
# fileBai=open('euskarazkoLabelaBai.csv', 'w', newline='')

# writerEz = csv.writer(fileEz)
# writerBai = csv.writer(fileBai)

# for taldea in datuak:
#     taldeIzena = taldea['izena'] + " "
#     emaitza = bilaketakFuntzioak.wikidatanDago(taldeIzena);
#     if emaitza is False:
#         writerEz.writerow([taldea['id'], taldea['izena'],taldea['biografia'], taldea['urtea'], taldea['herria'], taldea['generoak'], taldea['url']])
#     else:
#         writerBai.writerow([taldea['id'], taldea['izena'],taldea['biografia'], taldea['urtea'], taldea['herria'], taldea['generoak'], taldea['url']])



        
        
#  HAU LEHEN GENEUKANA DA, IUAL BEANDUO BERKO DEU
# # Taldeen CSVa ireki
# with open('D:/SourceTree/WikiBadok/taldeak.csv', 'r') as file:
#     csvreader = csv.reader(file)
#     # Errenkada bakoitzeko izena taldeak[] bektorean sartu
#     for row in csvreader:
#         taldeIzena = row[1]
#         taldeak.append(taldeIzena)
#         # Ongi sartuta dauden taldeak
#         with open('./ondo.csv', 'w', newline = '') as ondo:
#             writerOndo = csv.writer(ondo)
#             # Ez dauden taldeak
#             with open('./ezDago.csv', 'w', newline = '') as ezDago:
#                 writerEzDago = csv.writer(ezDago)
#                 # Musikariak ez diren taldeak
#                 with open('./arraro.csv', 'w', newline = '') as arraro:
#                     writerArraro = csv.writer(arraro)
#                     for t in taldeak:
#                         emaitzak = bilaketakFuntzioak.wikidatanDago(t) #Funtzioari deitu
#                         for taldeOrriak in emaitzak : #[orria1, orria2, ...]
#                             for orria in taldeOrriak: #[ID, label, description]
#                                 # 1. ez dago ezer
#                                 if(orria[0] == 'EzDago'): #Ez du ID
#                                     writerEzDago.writerow(orria)                    
#                                 # 2. KEYERROR 
#                                 elif orria[1] == 'KeyError' or orria[2] == 'KeyError':
#                                     # KEYERROR AZTERTZEKO FUNTZIOA
#                                     print("KEYERROR")
#                                 # 3. musikaria da?
#                                 elif 'musikari' in orria[2] or 'kantari' in orria[2] or 'abeslari' in orria[2] or 'talde' in orria[2]:
#                                     writerOndo.writerow(orria)
#                                 else:
#                                     writerArraro.writerow(orria) # Beste guztiak
#                 arraro.close()
#             ezDago.close()
#         ondo.close()
#     file.close()
