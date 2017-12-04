
#hapax2.py: copy hapax1.py and try to move well-defined steps from your legomena function
# (reading and cleaning the input text, making a frequency dictionary) into separate functions,
#  which are then called in the legomena function.
#  This is called code refactoring: splitting multi-step functionality over several functions.
#  This is good practice, and will make the next exercise much easier.



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

def legomena (filename):
    dict_tokens = frequency_dictionary(filename)
    list_hapax = []
    for key in dict_tokens:
        if dict_tokens[key]==1:
            list_hapax.append(key)

    return list_hapax

filename ="ThePictureOfDorianGray.txt"
result = legomena(filename)
print (result)