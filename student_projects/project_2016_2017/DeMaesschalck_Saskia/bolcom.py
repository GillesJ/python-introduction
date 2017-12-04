#https://www.bol.com/nl/s/algemeen/zoekresultaten/Ntt/the%2Bprice%2Bof%2Bsalt

import bs4
import requests

def find_bolcom(book_title):
    book_title = book_title.replace(" ", "%2B")
    book_title = book_title.lower()
    url_query = "https://www.bol.com/nl/s/algemeen/zoekresultaten/Ntt/" + book_title
    print(book_title)
    print(url_query)
    r = requests.get("https://www.bol.com/nl/s/algemeen/zoekresultaten/Ntt/" + book_title)
    html = r.text
    soup = bs4.BeautifulSoup(html, "lxml")
    books = soup.find("span", {"itemprop": "price"})
    print(books)

    
book_title = input("What book are you looking for? ")
find_bolcom(book_title)