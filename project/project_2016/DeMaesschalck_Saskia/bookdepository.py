import bs4
import requests

def find_bookdepository(book_title):
    book_title = book_title.replace(" ", "+")
    book_title = book_title.lower()
    r = requests.get("http://www.bookdepository.com/search?searchTerm=" + book_title + "&search=Find+book")
    html = r.text
    soup = bs4.BeautifulSoup(html, "lxml")
    books = soup.find("p", {"class": "price"})
    print(books)

    
book_title = input("What book are you looking for? ")
find_bookdepository(book_title)