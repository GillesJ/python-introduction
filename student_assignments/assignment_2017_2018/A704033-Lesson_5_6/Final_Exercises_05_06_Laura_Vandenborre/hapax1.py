# this works in Python notebooks, but not in Sublime Text for some reason, I was not able to solve the error

import string
import codecs
def legomena(filename):
	f = codecs.open(filename, "r", "utf-8")
	text = f.read()
	f.close()

translator = str.maketrans("", "", string.punctuation)
no_punct = text.translate(translator)
words = no_punct.lower().split()

freq_dict = {}
for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

for key, value in freq_dict.items():
    if value == 1:
        print(key)