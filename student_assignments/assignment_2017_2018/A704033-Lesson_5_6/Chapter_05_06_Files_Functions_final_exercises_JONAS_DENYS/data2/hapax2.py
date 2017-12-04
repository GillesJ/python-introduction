#VAN DEZE OEFENING KLOPT HELEMAAL NIKS

def openclean(file):
	import codecs
	f = codecs.open(file, 'r', 'utf-8')
	m = f.read()
	f.close()
	#print(input)
	m = m.lower()
	#print(input)

	import string
	exclude = set(string.punctuation)
	m = ''.join(ch for ch in m if ch not in exclude)
	#print(input)
	return m

def diction(file):
	from hapax2 import openclean
	openclean(file)
	freq = {}
	words = file.split()
	for word in words:
		if word not in freq:
			freq[word] = 1
		else:
			freq[word] += 1
	return freq

def output(file):
	from hapax2 import openclean
	from hapax2 import diction
	openclean(file)
	diction(file)
	output = []
	for word in freq:
		if freq[word] == 1:
			output.append(word)
	return output

def legomena(file):
	from hapax2 import openclean
	openclean(file)
	from hapax2 import diction
	diction(file)
	from hapax2 import output
	output(file)

print(legomena("marathon2.txt"))