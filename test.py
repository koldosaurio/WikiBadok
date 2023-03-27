
import pywikibot
"""
Adds claim to item
"""
site = pywikibot.Site("test", "wikidata")
repo = site.data_repository()
item = pywikibot.ItemPage(repo, "Q229612")


claim = pywikibot.Claim(repo, u'P131') #Adding located in the administrative territorial entity (P131)
target = pywikibot.ItemPage(repo, u"Q350") #Connecting P131 with Cambridge (Q350), who is a Q-id.
claim.setTarget(target) #Set the target value in the local object.

item.addClaim(claim, summary=u'Adding claim to Q229612') #Inserting value with summary to Q210194