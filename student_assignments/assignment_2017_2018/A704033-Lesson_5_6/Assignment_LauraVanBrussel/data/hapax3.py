#hapax3.py: copy hapax2.py and create two additional functions:
#  one that spots hapax dislegomena (words occuring only twice)
#  and one that spots hapax trislegomena (words occuring only three times) in a text file.

def reading_and_cleaning (filename):
    import codecs
    import re

    f= codecs.open (filename, "r","utf-8")
    t_input = f.read ()
    f.close()

    list_tokens_clean=re.findall(r"[\w']+|[.,!?;]", t_input.lower()) # separates words from punctuation marks
    return list_tokens_clean

def frequency_dictionary(filename):
    dict_tokens = {}
    import string
    list_tokens_clean = reading_and_cleaning(filename)
    for token in list_tokens_clean:
        if token not in string.punctuation: #you don't want to include punctuation marks in your dictionary
            if token not in dict_tokens:
                dict_tokens[token]=1
            elif token in dict_tokens:
                dict_tokens[token]= dict_tokens[token]+ 1
    return dict_tokens

def legomena(filename):
    dict_tokens = frequency_dictionary(filename)

    list_hapax = []

    for key in dict_tokens:
        if dict_tokens[key]==1:
            list_hapax.append(key)
    return list_hapax

def dislegomena(filename):
    dict_tokens = frequency_dictionary(filename)

    list_hapax_dislegomena=[]
    for key in dict_tokens:
        if dict_tokens[key]==2:
            list_hapax_dislegomena.append(key)
    return list_hapax_dislegomena

def trislegomena(filename):
    dict_tokens = frequency_dictionary(filename)

    list_hapax_trislegomena = []
    for key in dict_tokens:
        if dict_tokens[key] == 3:
            list_hapax_trislegomena.append(key)
    return list_hapax_trislegomena

#filename ="ThePictureOfDorianGray.txt"
#result1 = legomena(filename)
#print (result1)
#result2= dislegomena(filename)
#print (result2)
#result3 = trislegomena(filename)
#print (result3)

