def legomena_read(lego):
    import codecs
    import string
    filename = input('Enter your filename here with the directory. ')
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
    f.close()
    return text

#Lego Clean
def legomena_clean(lego):
    import codecs
    import string
    filename = input('Enter your filename here with the directory. ')
    f = codecs.open(filename , 'r' , 'utf-8')
    text = f.read()
    text_clean = text.strip()
    f.close()
    return text_clean

#Lego Freq
def legomena_freq(lego):
    import codecs
    import string
    filename = input('Enter your filename here with the directory as .txt file . ')
    f = codecs.open(filename + '.txt' , 'r' , 'utf-8')
    text = f.read()
    t_in_text = text.split()
    freq_list = []
    for i in t_in_text:
        token = t_in_text.count(i)
        freq_list.append((i,token))
    f.close()
    return freq_list