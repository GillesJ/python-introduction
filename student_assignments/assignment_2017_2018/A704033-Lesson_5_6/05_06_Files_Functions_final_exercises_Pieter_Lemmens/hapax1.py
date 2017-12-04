import codecs, string

def legomena(filename):
    filename = "data/frankenstein.txt"
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
   
    transl = str.maketrans('','', string.punctuation)
    text2 = text.translate(transl)
    text1 = text2.lower()

    freq = []
    t_in_text = text1.split()
    for word in t_in_text:
        token = t_in_text.count(word)
        if token < 2:
            freq.append((word,token))
    f.close()
    return freq

print(legomena('data/frankenstein.txt'))