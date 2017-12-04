import codecs, string

def legomena(filename):
    filename = input('Enter file path: ')
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
   
    transl = str.maketrans('','', string.punctuation)
    text2 = text.translate(transl).lower().split()

    freq = []
    for word in text2:
        token = text2.count(word)
        if token < 2:
            freq.append((word,token))
    f.close()
    return freq

def dislegomena(filename):
    filename = input('Enter file path: ')
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
   
    transl = str.maketrans('','', string.punctuation)
    text2 = text.translate(transl).lower().split()

    freq2 = []
    for word in text2:
        token = text2.count(word)
        if token == 2:
            freq2.append((word,token))
    f.close()
    return freq2

def trislegomena(filename):
    filename = input('Enter file path: ')
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
   
    transl = str.maketrans('','', string.punctuation)
    text2 = text.translate(transl).lower().split()

    freq3 = []
    for word in text2:
        token = text2.count(word)
        if token == 3:
            freq3.append((word,token))
    f.close()
    return freq3