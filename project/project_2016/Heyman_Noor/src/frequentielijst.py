'# coding=utf-8'
import codecs
frequentielijst = codecs.open ('data/CREA_freq.txt', 'r', 'latin1') #BD added data/
list_frequentie = frequentielijst.readlines()
list_frequentie = list_frequentie[:150] #lijn nadien verwijderen, anders moet alles ingeladen worden. Code is ook getest met meer en minder input.


dictionary_frequentie = {}
for line in list_frequentie:
	if line.strip():
		key, frequentie = line.split() #benoem de values als 'frequentie', omdat dat duidelijker is (de values van de dict zijn frequenties)
		dictionary_frequentie[key] = int(frequentie.strip()) #integers maken van de values als de dictionary wordt ingeladen
	


meest_frequente_woorden = []

frequente_woorden = []

minst_frequente_woorden = []


for word in dictionary_frequentie.keys(): #BD Harde cutoffs ipv rank-based
	if dictionary_frequentie[word] <= 9999518 and dictionary_frequentie[word] >= 1019669:
		print(word + " " + "is extreem frequent")
		meest_frequente_woorden.append(word)
	elif dictionary_frequentie[word] < 1019669 and dictionary_frequentie[word] >= 1004103:
		print (word + " " + "is zeer frequent")
		meest_frequente_woorden.append(word)
	elif dictionary_frequentie[word] < 1004103 and dictionary_frequentie[word] >= 10000:
		print (word + " " + "is frequent")
		frequente_woorden.append(word)
	elif dictionary_frequentie[word] < 10000 and dictionary_frequentie[word] >= 900:
		print (word+ " " + "is minder frequent")
		frequente_woorden.append(word)
	elif dictionary_frequentie[word] < 900 and dictionary_frequentie[word] >= 90:
		print (word+ " " + "is extreem infrequent")
		minst_frequente_woorden.append(word)
	elif dictionary_frequentie[word] < 90:
		print (word + " " + "is verwaarloosbaar")
		minst_frequente_woorden.append(word)

print(meest_frequente_woorden)
print(frequente_woorden)
print(minst_frequente_woorden)





