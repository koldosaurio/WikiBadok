# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 19:19:00 2023

@author: Lorea
"""

import pwbFuntzioak as funtzioak
import pywikibot

site = pywikibot.Site("test", "wikidata")
izena='Badok Proba 2'
statementCode='P94318'
targetCode='Q1785'

itemCode ='Q229997'

#funtzioak.add_statement(site, itemCode, statementCode, targetCode)

funtzioak.add_dateStatement(site, itemCode, 'P94385', 2023)

#funtzioak.add_reference(site, itemCode, statementCode, targetCode, 'https://es.wikipedia.org/wiki/Harry_Styles')