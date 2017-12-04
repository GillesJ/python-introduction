import codecs

def legomena(f):
	f = codecs.open('data/Sense and Sensibility.txt','r', 'utf-8')
	text = f.read()
	f.close()
	
	words = text.lower().split()
	
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	

	hapaxes = []
	for w in freqs:
		if freqs[w] == 1:
			hapaxes.append(w)
	return hapaxes

print(legomena("Sense and Sensibility.txt"))

def dislegomena(f):
	f = codecs.open('data/Sense and Sensibility.txt','r', 'utf-8')
	text = f.read()
	f.close()
	
	words = text.lower().split()
	
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	

	hapaxes = []
	for w in freqs:
		if freqs[w] == 2:
			hapaxes.append(w)
	return hapaxes

def trislegomena(f):
	f = codecs.open('data/Sense and Sensibility.txt','r', 'utf-8')
	text = f.read()
	f.close()
	
	words = text.lower().split()
	
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	

	hapaxes = []
	for w in freqs:
		if freqs[w] == 3:
			hapaxes.append(w)
	return hapaxes