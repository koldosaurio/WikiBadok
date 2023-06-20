# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:51:26 2023

@author: Koldo
"""
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

sparql.setQuery("""
SELECT ?item ?itemLabel
WHERE
{
    ?item wdt:P31 wd:Q146 .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()