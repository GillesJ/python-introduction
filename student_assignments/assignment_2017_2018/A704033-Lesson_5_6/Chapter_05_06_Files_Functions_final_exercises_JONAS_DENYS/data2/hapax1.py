def legomena(file):
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
	
	freq = {}
	words = m.split()
	for word in words:
		if word not in freq:
			freq[word] = 1
		else:
			freq[word] += 1
	
	output = []
	for word in freq:
		if freq[word] == 1:
			output.append(word)
	return output

print(legomena("marathon2.txt"))