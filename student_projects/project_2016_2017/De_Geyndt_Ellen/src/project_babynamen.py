def letters_naam(): #Vraag aan de gebruiker met welke letters de naam moet beginnen/eindigen
	lijst_eerste_letters = [] #BD hoeven geen lijsten te zijn, maar strings (telkens maar 1 element)
	eerste_letters = input("Met welke letter(s) moet de naam beginnen? Geef geen input indien het niet uitmaakt. ")
	lijst_eerste_letters.append(eerste_letters)
	lijst_laatste_letters = []
	laatste_letters = input("Met welke letter(s) moet de naam eindigen? Geef geen input indien het niet uitmaakt. ")
	lijst_laatste_letters.append(laatste_letters)
	return lijst_eerste_letters, lijst_laatste_letters

lijst_eerste_letters, lijst_laatste_letters = letters_naam()

def website_ophalen(letters_naam): #Creëer de website met de namen en crawl de data
	import requests #BD argument letters_naam wordt niet gebruikt!
	import bs4
	eerste_letters = "".join(lijst_eerste_letters) #BD gebruik gemaakt van globale variabele ipv argument; lijst bevat maar 1 element
	laatste_letters = "".join(lijst_laatste_letters)
	link = "http://www.babybytes.nl/namen/?searchnames=1&begins_with=" + eerste_letters + "&ends_with=" + laatste_letters #Combineert de website met de letters die ingegeven werden door de gebruiker
	r = requests.get(link)
	html = r.text
	parsed = bs4.BeautifulSoup(html, "lxml")
	return parsed #BD goeie variabelenamen

website = website_ophalen(letters_naam)

def titel_printen(website): #Print de titel van de pagina, waardoor de gebruiker meteen te zien krijgt hoeveel namen er beschikbaar zijn.
	for title in website.find_all("title"):
		print(title.text.strip("<title>"))

titel = titel_printen(website) #BD titel_printen returnt None, dus variabele "titel" is overbodig hier

def lijst_namen(website): #Print de lijst van de namen, gesplitst in jongens- en meisjesnamen
	from unidecode import unidecode
	list_names_boys = []
	list_names_girls = []
	for name in website.find_all("span", {"class": "babyname-page__name-experience__body__title boy"}):
		list_names_boys.append(name)
	for name in website.find_all("span", {"class": "babyname-page__name-experience__body__title girl"}):
		list_names_girls.append(name)
	jongensnamen = [name.text.strip("<>") for name in list_names_boys] #BD list comprehension, nice
	jongensnamen = ", ".join(jongensnamen)
	jongensnamen = unidecode(jongensnamen) #Haalt accenten weg. Zonder deze stap genereerde cmd een fout wanneer er speciale leestekens (accenten/aanhalingsteken) in de lijst voorkwamen.
	meisjesnamen = [name.text.strip("<>") for name in list_names_girls]
	meisjesnamen = ", ".join(meisjesnamen)
	meisjesnamen = unidecode(meisjesnamen)
	print("Voor jongens: ", jongensnamen, "\nVoor meisjes: ", meisjesnamen)

namen = lijst_namen(website) #BD opnieuw, lijst_namen heeft geen return value.

