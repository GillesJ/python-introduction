import codecs
import string

def open_file (filename):
    print("reading file")
    f = codecs.open(filename, 'r', 'utf-8')
    text = f.read()
    f.close()
    return text
   
def lower_list(text):
    print("removing cases")
    new_text = ""
    for char in text:
        if char not in string.punctuation:
            new_text+=char.lower()
    words = new_text.split()
    return words
    
def frequency_dictionary(words):
    print("frequency dictionary")  
    freqs = {}
    for w in words:
        try:
            freqs[w]+=1
        except KeyError:
            freqs[w]=1
    return freqs             

def hapaxes(freqs):  
    print("list with hapaxes") 
    list_hapaxes = []
    for w in freqs:
        if freqs[w] == 1:
            list_hapaxes.append(w)
    return list_hapaxes

def legomena(filename):
    text = open_file(filename)
    words = lower_list(text)
    freqs = frequency_dictionary(words)
    list_hapaxes = hapaxes(freqs)
    return list_hapaxes

filename = "gutenberg.txt"
output = legomena(filename)
g = codecs.open("hapax2.txt", 'w', 'utf-8')
g.write(str(output))
g.close
