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

print(legomena('data/frankenstein.txt'))