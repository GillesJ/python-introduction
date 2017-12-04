#!/usr/bin/env/ python 

def legomena(f):
	import codecs
	file = codecs.open(f, 'r', 'utf-8')
	t_in = file.read()
	file.close()

	t_in = t_in.lower()

	import string
	exclude = set(string.punctuation)
	t_in = ''.join(ch for ch in t_in if ch not in exclude)
	
	freq = {}
	words = t_in.split()

	for word in words:
		if word not in freq: 
			freq[word]=1
		else:
			freq[word]+=1

	legomena = []
	for word in freq:
		if freq[word] == 1:
			legomena.append(word)
			
	return legomena

print(legomena("data/peterpan.txt"))