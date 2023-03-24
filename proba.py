from urllib.request import urlopen

url = "https://www.badok.eus/euskal-musikak/"
html = urlopen(url).read().decode("utf-8")

hasiera = len('<section class="letra_bakoitza " id="0">')+html.find('<section class="letra_bakoitza " id="0">')
amaiera = html.find('<section class="letra_bakoitza " id="Z">') + len('<section class="letra_bakoitza " id="Z">') + \
          html.find(html[html.find('<\\section'):])

print(html[hasiera:amaiera].replace('<p>', '\n'))
