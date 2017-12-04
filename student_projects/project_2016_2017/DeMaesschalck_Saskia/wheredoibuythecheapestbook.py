import bs4
import requests

book_title = input("What book are you looking for? ") #er mogen geen tikfouten instaan
#BD Beetje error handling eventueel

def find_bolcom(book_title):
    book_title = book_title.replace(" ", "%2B") #om de input om te zetten in de correcte url van de zoekresultaten
    book_title = book_title.lower() # idem
    r = requests.get("https://www.bol.com/nl/s/algemeen/zoekresultaten/Ntt/" + book_title) #haalt alle html op van de zoekresultatenpagina
    html = r.text
    soup = bs4.BeautifulSoup(html, "lxml")
    book_price = soup.find("span", {"itemprop": "price"}) #bij bol.com is het eerste boek altijd het goedkoopste fysieke boek
    book_price = book_price.text.strip() #overbodige spaties verwijderen
    book_prices_list = [book_price] #lijst maken van book prices
    return book_prices_list

book_prices_list = find_bolcom(book_title) #variabele toekennen aan de eerste functie om ze te kunnen gebruiken in de volgende functie
#BD geen error handling als een website een boek niet heeft.

def find_bookdepository(book_title, book_prices_list):
    book_title = book_title.replace(" ", "+") #om de input om te zetten in de correcte url van de zoekresultaten
    book_title = book_title.lower()
    r = requests.get("http://www.bookdepository.com/search?searchTerm=" + book_title + "&search=Find+book") #haalt alle html op van de zoekresultatenpagina
    html = r.text
    soup = bs4.BeautifulSoup(html, "lxml")
    book_prices = soup.find_all("p", {"class": "price"}) #findall omdat bij bookdepository niet altijd het eerste boek goedkoper is
    for book_prices2 in book_prices: #BD book_prices2 is wat verwarrend als naam: is telkens maar 1 price
        book_prices2 = book_prices2.text.strip() #alle book_prices maar dan alleen de relevante text in de html
        book_prices_list.append(book_prices2) #de book prices van de boeken op bookdepository worden toegevoegd aan de lijst waar de prijs van op bol.com al in staat
    return book_prices_list

book_prices_list = find_bookdepository(book_title,book_prices_list) #variabele toekennen aan de tweede functie om ze verder te kunnen gebruiken
#BD deze manier van werken (book_prices_list als extra argument) veronderstelt dat je altijd bolcom zal opzoeken voordat je bookdepository gebruikt. Beter om beide functies identiek te maken qua structuur, en de resultaten te appenden aan een lijst die buiten de functies bestaat.
print(book_prices_list) #BD

def prices_cleaned(book_prices_list): #de output zit nog vol met symbolen en spaties die er niet thuishoren
    book_prices_list = [price.replace(",",".") for price in book_prices_list] #alle komma's worden vervangen door punten om de correcte Engelse spelling van cijfers te krijgen
    book_prices_list = [price.replace("€","") for price in book_prices_list] #alle eurotekens worden verwijderd
    book_prices_list = [price.replace("US$","") for price in book_prices_list] #BD alle dollartekens worden verwijderd
    book_prices_list = [price.replace("\n","") for price in book_prices_list] #alle \n'en worden verwijderd #BD met strip()?
    book_prices_list = [price.replace("                            \xa0","") for price in book_prices_list] #alle \xa0 met gigantisch veel spaties voor worden verwijderd, maar de karakters na de \xa0 bljven wel nog staan #BD ook op te lossen met strip(): \xa0 is een non-breaking space
    new_list =[]
    for price in book_prices_list:
        new_list.append(float(price[0:4])) #alleen de eerste 5 #BD 4 karakters omdat een prijs max. 4 karakters is, dus nu zijn ook de karakters die oorspronkelijk na de \xa0 stonden weg #BD werkt niet meer precies met boeken die overal meer dan 100 euro kosten. Moest ook [0:5] zijn
    cheapest_book = min(new_list[0:5]) #de eerste prijzen van de lijst zijn de relevantste, omdat eerst de paperbacks, daarna de hardcovers en daarna de e-books in de zoekresultaten staan. Wij hebben enkel de prijzen van paperbacks nodig #BD dit zijn niet de eerste 3, maar eerste 4 resultaten van bookdepository
    if cheapest_book == new_list[0]: #BD wat als ze allebei even goedkoop zijn? Bias voor Bol.com
        print("Bol.com: " + str(cheapest_book))#als het goedkoopste boek het eerste (nulde) element van de lijst is, dan is het sowieso het boek van bol.com 
    else:
        print("Bookdepository: " + str(cheapest_book)) #als het boek niet het eerste element is, dan is het sowieso van bookdepository #BD tuples bijhouden van prijs + titel zou hier interessant geweest zijn. Zou ook niet meer werken als bol.com (of een andere website) mogelijks meer dan 1 resultaat geven
    
prices_cleaned(book_prices_list)