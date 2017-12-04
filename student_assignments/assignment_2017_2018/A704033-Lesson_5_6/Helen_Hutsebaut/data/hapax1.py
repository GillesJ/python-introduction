def legomena (filename):
    import codecs
    f = codecs.open(filename, 'r', 'utf-8')
    text = f.read()
    f.close()
    
    import string
    new_text = ""
    for char in text:
        if char not in string.punctuation:
            new_text+=char.lower()
    words = new_text.split()
  
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

print(legomena("gutenberg.txt"))