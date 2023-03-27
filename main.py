import proba

#print(proba.izenak_lortu())
for i in proba.izenak_lortu():
    print(proba.taldearen_diskoak_lortu(i['url'].replace(' ','%20')))

