#!/usr/bin/env/ python 
# -*- coding: utf-8 -*-

# THIS SCRIPT CHECKS IF THE LEMMATA ARE ALSO IN THE LEXICONS (POSITIVE AND NEGATIVE)
# IF IT IS IN THE POSITIVE LEXICON, IT PRINTS THE WORD WITH A + NEXT TO IT
# IF IT IS IN THE NEGATIVE LEXICON, IT PRINTS THE WORD WITH A - NEXT TO IT
# IF IT IS NOT IN THE LEXICON, IT PRINTS 'LEMMA IS NOT IN ONE OF THE LEXICONS'

import codecs

# read the positive words
p = codecs.open("SpanishSentimentLexicons/pos_words.txt", "r", "utf-8")
pos_words = p.read()
p.close()

# read the negative words
n = codecs.open("SpanishSentimentLexicons/neg_words.txt", "r", "utf-8")
neg_words = n.read()
n.close()

c=0
while c<5:
	c+=1 
	for file in ".\\tag_docs\\":
		# read the lemmata
		h = codecs.open(".\\tag_docs\\lemmata\\article" + str(c) + "_lemmata.txt", "r", "utf-8")
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
		o = codecs.open(".\\tag_docs\\final_output\\article" + str(c) + "_final_output.txt", 'w', 'utf-8')
		o.write('\n'.join(output) + '\n\n' + 'The total value of this article is: ' + str(k))
		o.close()