import codecs
seenorunseenlist = codecs.open('data/Ugent niveaulijst.txt', 'r', 'utf-8') #BD added data/
seenorunseenlist = seenorunseenlist.readlines()

dictionary_seenorunseen = {}
for line in seenorunseenlist:
	if line.strip(): #zodra de lijn gesplit is... #BD als de lijn niet leeg is...
		key, value = line.split()
		dictionary_seenorunseen[key] = str(value.strip()) #strings als resultaat
#BD identieke functionaliteit als dictionary_niveaulijst; verschilt enkel in filepath. Functie maken dat obv filepath een dictionary returnt


woord = input ("Welk woord wil je opzoeken? ") #input getest in een notebook
if woord in dictionary_seenorunseen:
	print(woord + " zit in het woordenboek")
else:
	print (woord + " zit NIET in het woordenboek")

#BD functie van maken

