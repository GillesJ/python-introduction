def length(): #Aan de gebruiker vragen hoe lang het woord is
	lengte = input("Hoe lang is je woord? ")
	lengte = int(lengte) #Int van de string maken, zodat we het later als getal kunnen gebruiken
	#BD eventueel error handling hier als de input niet valide is
	return lengte

lengte_woord = length()

def letter_in_place(lengte_woord): #Aan de gebruiker vragen welke letters hij kent
	letters = [	]
	index = 0
	while index < lengte_woord:
		letter = input("Wat is letter " + str(index + 1) + "? (zet een punt bij onbekende letters) ")
		letters.append(letter)
		index = index + 1 #BD of shortcut +=
	return letters

letters = letter_in_place(lengte_woord)

def woordenboek(): #Woordenlijst inlezen
	import codecs
	f = codecs.open("data/woordenlijst.txt" , "r" , "utf8" ) #BD \ naar / veranderd voor Mac
	list_words = f.readlines()
	f.close()
	words = [word.strip("\n") for word in list_words] #In het origineel document stond elk woord op een aparte lijn, waardoor python de enter als één van de karakters van het woord telde
	return words

words = woordenboek()

def mogelijke_woorden(lengte_woord, letters, words): #Mogelijke woorden weergeven
	from unidecode import unidecode
	possible_words = []
	for word in words:
		if len(word) == lengte_woord:
			woord_als_lijst = list(word) #Het woord uit de woordenlijst weergeven als een lijst, zo kan het vergeleken worden met de lijst letters die eerder ingegeven werden
			checks = []
			for letter_woord, gegeven_letter in zip(woord_als_lijst, letters):
				letter_woord = letter_woord.lower() # + de volgende stap: hoofdletters wegwerken in beide lijsten, om meer kans te hebben op een match
				gegeven_letter = gegeven_letter.lower()
				letter_woord = unidecode(letter_woord) # + de volgende stap: accenten, umlauts,... wegwerken om meer kans te hebben op een match (indien gebruikers geen accent ingeven)
				gegeven_letter  = unidecode(gegeven_letter)
				if letter_woord == gegeven_letter:
					checks.append("true") #BD liever een echte Boolean gebruiken
				elif gegeven_letter == ".":
					checks.append("true")
				else:
					checks.append("false")
			if "false" not in checks:
				possible_words.append(word)
	possible_words = sorted(possible_words, key=str.lower) #lijst alfabetisch ordenen en hoofdletters op dezelfde manier verwerken als kleine letters
	print(possible_words) #BD Pretty print zou hier beter geweest zijn; aantal hits; message als er geen enkele hit is

mogelijke_woorden(lengte_woord, letters, words) #BD Mooi dat je hier alles meegeeft, zodat mogelijke_woorden niet met globale variabelen moet werken



