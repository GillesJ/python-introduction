#hapax1.py: a hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language,
# the works of an author, or in a single text.
# Define a function legomena that given the filename of a text will return a list of all its hapax legomena.
#  Make sure your program ignores capitalization as well as punctuation (hint: check out string.
# punctuation online!). Try out the function on your Gutenberg book from the previous Chapter.
# For simplicity, make sure your Gutenberg file is in the same directory as your hapax script,
# so that you can just use the file's name as a relative path.
#  Alternatively, you can use an absolute path to the file.
def legomena (filename):
    import codecs
    f= codecs.open (filename, "r","utf-8")
    t_input = f.read ()
    f.close()

    import re
    list_tokens_original=re.findall(r"[\w']+|[.,!?;]", t_input.lower())
    dict_tokens ={} #without punctuation marks, extra spaces: the pure words in lower case.

    import string
    for token in list_tokens_original:
        if token not in string.punctuation:
            if token not in dict_tokens:
                dict_tokens[token]=1
            elif token in dict_tokens:
                dict_tokens[token]= dict_tokens[token]+ 1


    list_hapax = []
    for key in dict_tokens:
        if dict_tokens[key]==1:
            list_hapax.append(key)
    return list_hapax

filename ="ThePictureOfDorianGray.txt"
result = legomena(filename)
print (result)