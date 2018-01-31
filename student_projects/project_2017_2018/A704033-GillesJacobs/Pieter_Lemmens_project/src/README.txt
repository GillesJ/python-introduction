------------------------------------------------------------------------------------------------------------------------------------------------------------------
PROJECT
------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project's original goal was to create a script that would allow the user to fetch user book reviews given the title of a book. Both Goodreads and LibraryThing were supposed to serve as sources for reviews, but this project turned out to be a lot more complicated as was foreseen initially. 
There were many limitations and problems (deprecated or unmaintained APIs, API methods simply not working, ...) that held me back from using LibraryThing as a second primary source for book reviews, and working with Goodreads own API turned out to be fairly complex too. Thus, I decided to restrict the project to Goodreads only. I have tried looking for alternative services (such as aNobii and some ebook websites), but they either did not have an API that was functioning, or the amount of data they had was lacklustre.

I believe there are no additional dependencies than what is found in the Python standard library (Regex, requests, BeautifulSoup4, ElementTree, and urllib)
------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSTRUCTIONS
------------------------------------------------------------------------------------------------------------------------------------------------------------------
To use the program, simply run goodreads.py. Usage should be fairly straightforward. The program should ask for an input which can either be a book title or an authro name. Once the input is given, it will display a list of the Goodreads book IDs that match the input 
To continue, pick the book you would like to see reviews for and copy the book ID (i.e. the string of numbers before the right-pointing arrow), then hit enter. If all goes well, the program will then serve you 10 reviews for the chosen book.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
ADDITIONAL NOTES
------------------------------------------------------------------------------------------------------------------------------------------------------------------
- In some cases the program will return nothing after entering the book ID, this is because the selected book has not been reviewed by any users.
- The search query is done using the Goodreads API, so I do not really have control over what books Goodreads decides to list first. However, this also means it does not matter whether the input contains capital letters or slight misspellings.
- An additional (and unfortunate) limitation of this project is that Goodreads makes it UNABLE to access more than 300 characters of every user review. In practice, this means that in the program only about the first two lines of every review will be displayed. The reviews I accessed in this program are part of a widget that websites can use to embed Goodreads reviews on their website. To gain access to more data, you need to be a whitelisted partner and/or sign up for an Amazon developer key.