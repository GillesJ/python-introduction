#!/usr/bin/env/ python 
# -*- coding: utf-8 -*-

import requests
import bs4
import codecs
import io
from def_scap_tagging import tagging
import os

#reading the positive words
p = codecs.open("SpanishSentimentLexicons/pos_words.txt", "r", "utf-8")
pos_words = p.read()
p.close()

#reading the negative words
n = codecs.open("SpanishSentimentLexicons/neg_words.txt", "r", "utf-8")
neg_words = n.read()
n.close()

#scraping the html of the webpage
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

t=0
while t<5:
	t+=1 
	for file in ".\\tag_docs\\":

		#tagging all scraped files, using treetagger (defined in def_scap_tagging.py)
		file = ".\\tag_docs\\article" + str(t) + ".txt"
		tagging(file)

		#reading all tagged files
		f=codecs.open(".\\tag_docs\\article" + str(t) + "_tag_cap.txt", "r", "utf-8")
		tagged_text = f.read()
		f.close()

		ver_sus_adj_adv = []
		otros = []

		# adding all nouns, adjectives, verbs and adverbs to one list, all the rest to another list
		for item in tagged_text.split('\n'):
			if "NC" in item:
				ver_sus_adj_adv.append(item)
			elif "ADJ" in item:
				ver_sus_adj_adv.append(item)
			elif "VLfin" in item:
				ver_sus_adj_adv.append(item)
			elif "VLinf" in item:
				ver_sus_adj_adv.append(item)
			elif "ADV" in item:
				ver_sus_adj_adv.append(item)
		
		lemmata = []

		# adding every lemma (= every third 'word') to a list
		for line in ver_sus_adj_adv:
			words = line.split()
			#print(words)
			#print(words[2])
			lemmata.append(words[2])

		# writing the list with all nouns, adjectives, verbs and adverbs to one file, writing the rest to another file
		s = codecs.open(".\\tag_docs\\ver_sus_adj_adv\\article" + str(t) + "_ver_sus_adj_adv.txt", "w", "utf-8")
		s.write('\n'.join(ver_sus_adj_adv))
		s.close()

		# writing the lemmata list to a file
		h = codecs.open(".\\tag_docs\\lemmata\\article" + str(t) + "_lemmata.txt", "w", "utf-8")
		h.write('\n'.join(lemmata))
		h.close()

		# read the lemmata
		h = codecs.open(".\\tag_docs\\lemmata\\article" + str(t) + "_lemmata.txt", "r", "utf-8")
		lemmata = h.read()
		h.close()

		output = []
		k = 0

		# if the lemma is in pos_words: append "lemma +" to output
		# if the lemma is in neg_words: append "lemma -" to output
		# if the lemma is in none of the lexicons: append "The lemma is not in one of the lexicons." to output
		for lemma in lemmata.split('\n'):
			if lemma == "<unknown>":
				pass
			elif lemma in pos_words:
				output.append(lemma + ' +')
				k += 1
			elif lemma in neg_words:
				output.append(lemma + ' -')
				k -= 1
			else:
				output.append('The lemma <' + lemma + '> is not in one of the lexicons.')

		# writing output to a file
		o = codecs.open(".\\tag_docs\\final_output\\article" + str(t) + "_final_output.txt", 'w', 'utf-8')
		o.write('\n'.join(output) + '\n\n' + 'The total value of this article is: ' + str(k))
		o.close()