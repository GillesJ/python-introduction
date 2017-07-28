#!/usr/bin/env/ python
import codecs
import string

def read_and_clean_text(filename):
	with codecs.open(filename, "r", "utf8") as f:
		text = f.read()
	for char in string.punctuation:
		text = text.replace(char, "") # Remove each punctuation character
	text = text.lower()
	return text

def make_frequency_dictionary(words):
	freq_dict = {}
	for word in words:
		if word not in freq_dict:
			freq_dict[word] = 1
		else:
			freq_dict[word] += 1
	return freq_dict

def legomena(filename):
	cleaned_text = read_and_clean_text(filename)
	words = cleaned_text.split()
	freq_dict = make_frequency_dictionary(words)
	legomena = []
	for word in freq_dict:
		if freq_dict[word] == 1:
			legomena.append(word)
	return legomena

print(legomena("earnest.txt"))
