import codecs

def legomena(f):
	f = codecs.open('data/Sense and Sensibility.txt','r', 'utf-8')
	text = f.read()
	f.close()
	
	words = text.lower().split()
	
def freq():
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	return freq[w]

def hapax():	
	hapaxes = []
	for w in freqs:
		if freqs[w] == 1:
			hapaxes.append(w)
	return hapaxes

print(legomena("Sense and Sensibility.txt"))