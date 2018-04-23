#!/usr/bin/env/ python 
# -*- coding: utf-8 -*-

# THIS SCRIPT SCRAPES THE FIRST 5 ARTICLES ON THE ECONOMY SECTION OF THE WEBSITE OF SPANISH NEWSPAPER EL PAÍS 
# AND STORES THE SCRAPING RESULTS IN A SEPARATE DOCUMENT PER ARTICLE

import requests
import bs4
import codecs
import io

r  = requests.get("https://elpais.com/economia/")
html = r.text 
soup = bs4.BeautifulSoup(html, "lxml")

titles = []
links=[]
c=0


#Scraping the title of the article and appending it to list 'info':
for title in soup.find_all("h2", {"class": "articulo-titulo"}, limit=5):
	info = []
	title_text = title.text.strip()
	title_text.encode('utf-8')
	info.append(title_text)

#Scraping the url of the article and appending it to 'links' and 'info'
	link = title.find("a")
	if link['href'].startswith("/economia/"):
		url = "https://elpais.com" + link['href']
		info.append(url)
		links.append(url)

#Scraping all "h2" titles (subtitles) and appending to 'info':
	t = requests.get(url)
	html = t.text
	soup = bs4.BeautifulSoup(html, "lxml")
	title = soup.find("h2")
	info.append(title.text.strip())

#Scraping the publication date of the article and appending to 'info':
	d = requests.get(url)
	html = d.text
	soup = bs4.BeautifulSoup(html, "lxml")
	date = soup.find("time")
	info.append((date.text).strip().replace("\t",""))
	info_str = '\n'.join(info)
	
#Counter so different filenames are automatically  + writing list 'info' to a txt doc: 
	c+=1
	f=codecs.open(".\\tag_docs\\article" + str(c) + ".txt", 'w', 'utf-8')
	f.write(info_str)
	f.close()

#Visiting each url in our list 'links'. For every url the script looks for an introduction.
#If introduction is found - append to list 'intro'. 
#If not: "no hay una introduccion". 
intro = []
for link in links:
	r = requests.get(link)
	html = r.text
	soup = bs4.BeautifulSoup(html, "lxml")	
	if 'class="articulo-introduccion"' in html:
		for introduccion in soup.find_all("div", {"class": "articulo-introduccion"}):
			intro.append(introduccion.text.strip())	
	else:
		intro.append("No hay una introducción.")	

#Writing the introduction to the correct file that already has the info of the article in it. 
filenames = ['article1.txt', 'article2.txt', 'article3.txt', 'article4.txt', 'article5.txt'] #this list has to be extended if we scrape more articles

for li_item, filename in zip(intro, filenames):
	f = codecs.open(".\\tag_docs\\" + filename, 'a', 'utf-8')
	f.write('\n' + li_item +'\n')
	f.close()
