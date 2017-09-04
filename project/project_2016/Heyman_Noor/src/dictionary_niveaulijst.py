import codecs
niveaulijst = codecs.open ('data/Ugent niveaulijst.txt', 'r', 'utf-8') #BD added data/; overbodige lijn want file object niveaulijst wordt niet gebruikt
list_niveau = open ("data/Ugent niveaulijst.txt").readlines() #BD added data/

dictionary_niveau = {}
for line in list_niveau:
	list_niveau_split = line.split("\t") #gesplit op tab om het overzichtelijker te maken, maar mag eigenlijk weg #BD variabele list_niveau_split wordt nergens gebruikt, dus mag inderdaad weg

	if line.strip(): #zodra de lijn gesplit is... #BD liever: als het geen lege lijn is...
		key, value = line.split() #BD liever duidelijke variabelenamen: lemma, niveau
		dictionary_niveau[key] = str(value.strip()) #strings als resultaat	

niveau = dictionary_niveau['abandono'] #een bepaalde key oproepen
print(niveau)


#def van maken #BD inderdaad










