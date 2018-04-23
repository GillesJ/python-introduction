#!/usr/bin/env/ python 
# -*- coding: utf-8 -*-

# THIS SCRIPT SORTS THE TREETAGGER OUTPUT: ALL NOUNS, ALL VERBS AND ALL ADJETIVES ARE WRITTEN TO THREE SEPERATE FILES
# ALL THE REST IS WRITTEN INTO A 4TH FILE, WHICH WE WON'T USE FURTHER ON

import codecs

c=0
while c<5:
	c+=1 
	for file in ".\\tag_docs\\":
		f=codecs.open(".\\tag_docs\\article" + str(c) + "_tag_cap.txt", "r", "utf-8")
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
		s = codecs.open(".\\tag_docs\\ver_sus_adj_adv\\article" + str(c) + "_ver_sus_adj_adv.txt", "w", "utf-8")
		s.write('\n'.join(ver_sus_adj_adv))
		s.close()

		# writing the lemmata list to a file
		h = codecs.open(".\\tag_docs\\lemmata\\article" + str(c) + "_lemmata.txt", "w", "utf-8")
		h.write('\n'.join(lemmata))
		h.close()