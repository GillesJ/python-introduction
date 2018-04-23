import requests
from bs4 import BeautifulSoup
import codecs
from def_scap_tagging import tagging
import json
from OpenDutchWordnet import Wn_grid_parser, synsets


#PART1: WEBSCRAPING
r = requests.get("http://www.femma.be/nl/blog/artikel/verhaal-van-verdriet-en-hoop")
html = r.text
soup = BeautifulSoup(html, "lxml")

webpage_p = soup.find_all('p')

webpage = []
string = ""
for p in webpage_p:
	paragraph = p.get_text()
	webpage.append(paragraph.encode('utf-8'))
	string = string + paragraph

total_words = (len(string.split()))

f = codecs.open('../data/output_webscraping.txt','w', 'utf-8')
f.write(string)
f.close()


#PART 2: TREETAGGER
file = '../data/output_webscraping.txt'
tagging(file)

tagged_file = codecs.open('../data/output_webscraping_tag_cap.txt','r', 'utf-8')
text = tagged_file.read()
tagged_file.close()


#PART 3: CLEAN OUTPUT TREETAGGER
text_split = text.split('\r\n')
wordlist = []
for l in text_split: 	
	l = l.split('\t')
	wordlist.append(l)

wordlist = wordlist[:-1]	#delete empty line at the end
	
freq_lem = {}	
search_pos = ['adj', 'nounsg', 'nounpl', 'nounprop']	#search for these word classes in output Treetagger and put them in dict (freq_lem)

for item in wordlist:
	if item[1] in search_pos:
		if item[2] in freq_lem:
			freq_lem[item[2]] += 1
		else: 
			freq_lem[item[2]] = 1		


#PART 4: WRITE CLEANED AND SORTED OUTPUT TO FILE (with json)
with open('../data/clean_tt_output.txt', 'w') as file:
     file.write(json.dumps(freq_lem))
file.close()


#PART 5: CALCULATE WORD FREQUENCY
for key in freq_lem:
	word_freq = (freq_lem[key]/total_words)*100
	freq_lem[key] = word_freq

high_freq = []			#if word_freq was higher than 1 -> add to high_freq
for key in freq_lem:
	if freq_lem[key] >= 1:
		high_freq.append(key)
if not high_freq:
	print("Proficiat, uw tekt is gevarieerd!")


#PART 6: SUGGEST SYNONYMS
for item in high_freq:
	lemma = item
	wn = Wn_grid_parser(Wn_grid_parser.odwn)
	synonyms = wn.lemma_synonyms(lemma)
	print(lemma)
	print(synonyms)