def legomena_dis(lego):
    import codecs
    import string
    filename = input('Enter your filename here with the directory as .txt file . ')
    f = codecs.open(filename + '.txt' , 'r' , 'utf-8')
    text = f.read()
    t_in_text = text.split()
    freq_list_dis = []
    for i in t_in_text:
        token = t_in_text.count(i)
        if token == 2:
            freq_list_dis.append((i,token))
    f.close()
    return freq_list_dis


def legomena_tris(lego):
    import codecs
    import string
    filename = input('Enter your filename here with the directory as .txt file . ')
    f = codecs.open(filename + '.txt' , 'r' , 'utf-8')
    text = f.read()
    t_in_text = text.split()
    freq_list_tris = []
    for i in t_in_text:
        token = t_in_text.count(i)
        if token == 3:
            freq_list_tris.append((i,token))
    f.close()
    return freq_list_tris

