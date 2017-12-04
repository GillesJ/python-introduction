import requests
import bs4
import codecs

def create_dicts(filename):
	f = codecs.open(filename, "r", "utf8")
	words = f.readlines()
	f.close()
	NC = {} #dictionary for NC
	ADJ = {} #dictionary for ADJ and ADJV
	V = {} #dictionary for V
	for word in words:
		word = "".join(word.split("\r\n"))
		word = word.split("\t") #each word is a list containing the word (index 0) and the word class (index 1)
		if word[1] == "NC":
			NC[word[0]] = word[1]
		elif word[1] == "V":
			V[word[0]] = word[1]
		elif word[1] == "ADJ" or "ADJV":
			ADJ[word[0]] = word[1]
	return NC, ADJ, V
	#I made three dictionaries, because some words can be used as a noun and an adjective (e.g. perro). Therefore, it was easier to create a dictionary for each word class.

def translate_mijnwoordenboek(filename):
	NC, ADJ, V = create_dicts(filename) #the returned dictionaries from the function are assigned to a variable.
	NC_tra = {} #this dictionary will contain the translations of the words in the NC dictionary. Actually, this dictionary is not necessary, but should it be necessary, the dictionary can be used.
	f_nc = codecs.open("output/NC_vertalingen.txt", "w", "utf8") #the file is created here, because each word is written separately to a file instead of writing 
	for word in NC.keys():
		tras = []
		r = requests.get("http://www.mijnwoordenboek.nl/vertaal/ES/NL/" + word)
		html = r.text
		soup = bs4.BeautifulSoup(html, "lxml")
		for word_class in soup.find_all(string=" zelfst.naamw."): #all nouns have this string as subline, but not in a tag.
			translation = word_class.next_sibling
			while (translation.name) not in ["h2", "span"]: #h2 is used for a new word, the "span" tag is used at the end of the translations part.
				if (translation.name) == "font":
					if translation["style"] == "color:navy;font-size:10pt": #the translations are between the tag "font" in that style.
						tr = translation.text.split(",")
						for i in tr:
							tras.append(i.strip())
				translation = translation.next_sibling
			NC_tra[word] = tras
		if not word in NC_tra: #should no translation be found where it should be on mijnwoordenboek.nl, this part looks for the translation in "Overige bronnen".
			if word == soup.find("span", {"class": "deel2"}): #e.g. the tranlsation for abarrote were those of abarrotar (v), deel2 contains the spanish word
				for translation in soup.find_all("span", {"class": "deel4"}): #deel4 contains all the translations
					tras.append(translation.text.strip())
		if tras:
			NC_tra[word] = tras
		else:
			NC_tra[word] = ["No translation on no mijnwoordenboek.nl"] #If no "normal" translation and no "overige bronnen" translation have been found.
		vertalingen = ", ".join(list(set(NC_tra[word])))
		v = word + "\t" + NC[word] + "\t" + vertalingen + "\n" #the NC[word], which displays the word class, is in fact unnecessary, but this way, the three documents can easily be merged without loss of information.
		f_nc.write(v)
	f_nc.close()
	ADJ_tra = {}
	f_adj = codecs.open("output/ADJ_vertalingen.txt", "w", "utf8")
	for word in ADJ.keys():
		tras = []
		r = requests.get("http://www.mijnwoordenboek.nl/vertaal/ES/NL/" + word)
		html = r.text
		soup = bs4.BeautifulSoup(html, "lxml")
		for word_class in soup.find_all(string=" bijv.naamw."): #I wanted to define a function for this part (i.e. lines 28-52 and 57-79),
			translation = word_class.next_sibling				#but I couldn't find how I could "generalise" the string, like if NC: name = " zeflst.naamw." // if ADJ: name = " bijv.naamw.".
			while (translation.name) not in ["h2", "span"]:		#Unfortunately, this did not work resulting in twice the same code, except for the string.
				if (translation.name) == "font":
					if translation["style"] == "color:navy;font-size:10pt":
						tras.append(translation.text.strip())
				translation = translation.next_sibling
			ADJ_tra[word] = tras
		if not word in ADJ_tra:
			if word == soup.find("span", {"class": "deel2"}):
				for translation in soup.find_all("span", {"class": "deel4"}):
					tras.append(translation.text.strip())
		if tras:
			ADJ_tra[word] = tras
		else:
			ADJ_tra[word] = ["No translations on mijnwoordenboek.nl"]
		vertalingen = ", ".join(list(set(ADJ_tra[word])))
		v = word + "\t" + ADJ[word] + "\t" + vertalingen + "\n"
		f_adj.write(v)
	f_adj.close()
	V_tra = {}
	f_v = codecs.open("output/V_vertalingen.txt", "w", "utf8")
	for word in V.keys():
		tras = []
		r = requests.get("http://www.mijnwoordenboek.nl/vertaal/ES/NL/" + word)
		html = r.text
		soup = bs4.BeautifulSoup(html, "lxml")
		for word_class in soup.find_all(string=" werkw."):
			t = [] #Also an additional list is created, as some verbs have more than one "h2" tag on mijnwoordenboek. However, this was not the case for the nouns and adjectives.
			translation = word_class.next_sibling
			if word_class.previous_element.strip() == word: #Because the translation of the reflexive verbs were also added (e.g. abrazar and abrazarse), this line was added.
				while (translation.name) not in ["h2", "span"]:
					if (translation.name) == "font":
						if translation["style"] == "color:navy;font-size:10pt":
							t.append(translation.text.strip())
					translation = translation.next_sibling
				tras.append(t)
				V_tra[word] = tras
		if word not in V_tra:
			t = []
			if word == soup.find("span", {"class": "deel2"}):
				for translation in soup.find_all("span", {"class": "deel4"}):
					t.append(translation.text.strip())
			if t:
				tras.append(t)
			else:
				tras.append(["No translation on mijnwoordenboek.nl"])
			V_tra[word] = tras
		#write to a file
		lijst = []
		for li in V_tra[word]:
			lijst.append(", ".join(list(set(li))))
		vertalingen = "\n\t\t".join(lijst) #By creating an extra list t, different translation can be displayed on separate lines in the txt file.
		v = word + "\t" + V[word] + "\t" + vertalingen + "\n"
		f_v.write(v)
	f_v.close()
	print("Hurray, the translations have been found as well.")