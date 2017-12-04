def legomena(lego):
    import codecs
    import string
    filename = input('Enter your filename here with the directory. ')
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
    translator = str.maketrans('','', string.punctuation)
    text2 = text.translate(translator)
    #The code translator works. My text is printed w/o any puntc.
    text1 = text2.lower()
    freq_list = []
    t_in_text = text1.split()
    for i in t_in_text:
        token = t_in_text.count(i)
        if token < 2:
            freq_list.append((i,token))
    f.close()
    return freq_list 
