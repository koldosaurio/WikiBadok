import proba

#print(proba.izenak_lortu())
datuak=proba.izenak_lortu()
# web orrian topatzen dituen izen guztiei diskak aldagaia gehituko die
for i in range(len(datuak)):
    datuak[i]['diskak'] = proba.taldearen_diskoak_lortu(datuak[i]['url'].replace(' ','%20'))
print(datuak)

