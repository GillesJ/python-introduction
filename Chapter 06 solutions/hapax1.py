#!/usr/bin/env/ python
import codecs
import string

def legomena(filename):
	# Read and clean the text
	with codecs.open(filename, "r", "utf8") as f:
		text = f.read()
	for char in string.punctuation:
		text = text.replace(char, "") # Remove each punctuation character
	text = text.lower()

	# Split text into words
	words = text.split()

	# Make a frequency dictionary
	freq_dict = {}
	for word in words:
		if word not in freq_dict:
			freq_dict[word] = 1
		else:
			freq_dict[word] += 1

	# Find the hapax legomena and put them in a list
	legomena = []
	for word in freq_dict:
		if freq_dict[word] == 1:
			legomena.append(word)

	# Return the result
	return legomena

print(legomena("earnest.txt"))
