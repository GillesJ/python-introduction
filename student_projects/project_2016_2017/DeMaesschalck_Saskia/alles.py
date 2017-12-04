import bs4
import requests

def find_bolcom(book_title):
    book_title = book_title.replace(" ", "%2B") 
    book_title = book_title.lower() # idem
    r = requests.get("https://www.bol.com/nl/s/algemeen/zoekresultaten/Ntt/" + book_title) 
    html = r.text
    soup = bs4.BeautifulSoup(html, "lxml")
    book_price = soup.find("span", {"itemprop": "price"}) 
    print("bol.com: " + book_price.text.strip()) 

def find_bookdepository(book_title):
    book_title = book_title.replace(" ", "+")
    book_title = book_title.lower()
    r = requests.get("http://www.bookdepository.com/search?searchTerm=" + book_title + "&search=Find+book")
    html = r.text
    soup = bs4.BeautifulSoup(html, "lxml")
    book_prices = soup.find_all("p", {"class": "price"}) 
    for book_price in book_prices:
        print("Bookdepository: " + book_price.text.strip())
    
book_title = input("What book are you looking for? ")

find_bolcom(book_title)
find_bookdepository(book_title)