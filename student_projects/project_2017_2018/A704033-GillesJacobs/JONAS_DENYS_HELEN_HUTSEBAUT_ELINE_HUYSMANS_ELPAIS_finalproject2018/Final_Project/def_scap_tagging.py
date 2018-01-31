import codecs
import os
import subprocess
import pickle
#from definities_algemeen import opencsv_as_list, dict_count, print_list_as_csv
import numpy
import json
import os.path
# import csv
# import xlsxwriter
# from collections import OrderedDict
# from operator import itemgetter
# from docx import Document


def preformat_replace(text): #NODIG in scrip preformat_preformat!
    text = text.replace("¿", "¿ ")
    text = text.replace('′', "'")
    text = text.replace('´', "'")
    text = text.replace('`', "'")
    text = text.replace("¡", "¡ ")
    text = text.replace("«", "« ")
    text = text.replace("»", " »")
    text = text.replace(" -", " - ")
    text = text.replace('- ', ' - ')
    text = text.replace('\n-', '\n- ')
    text = text.replace("-,", " -,")
    text = text.replace("-.", " -.")
    text = text.replace("—", " — ")
    text = text.replace(")", " ) ")
    text = text.replace("(", " ( ")
    text = text.replace("[", "[ ")
    text = text.replace("]", " ]")
    text = text.replace("\r\n", " ‡\r\n")
    text = text.replace("\r", " ‡\r")
    text = text.replace("\n", " ‡\n")
    text = text.replace(" ‡ ‡\r", " ‡\r")
    text = text.replace("\r ‡\n", "\r\n")
    text = text.replace("  ", " ")

    return text

def preformat(pr, file, type_pr):
    print("start preformat")
    if type_pr == 'Python_corp':
        inputfile = os.path.join('..', 'corpus', 'data', 'raw', pr, file)
        outputfile = os.path.join('..', 'corpus', 'data', 'work', pr, file)
        if os.path.isdir(os.path.join('..', 'corpus', 'data', 'work', pr)) == False:
            os.mkdir(os.path.join('..', 'corpus', 'data', 'work', pr))
    f = codecs.open(inputfile, 'r', 'utf-8-sig')
    text = f.read()
    f.close()
    text = preformat_replace(text)
    g = codecs.open(outputfile, 'w', 'utf-8-sig')
    g.write(text)
    g.close()

    return outputfile

#   return outputfile, path_out, path_workdocs, path_tag, path_ngrams, path_translat, path_voc_lists, path_voc_analysis

def tagging(file):
    print(file)
    tagger_cap = ".\\treetagger\\bin\\tag-spanish-cap.bat"
#    tagger_nocap = "C:\\Users\\pagoetha\\Documents\\SCAP\\treetagger\\bin\\tag-spanish-nocap.bat"
#    taggedfile_nocap = os.path.abspath(os.path.join(outputfile.replace(".txt", "_tag_nocap.txt")))
    taggedfile_cap = os.path.abspath(os.path.join(file.replace(".txt", "_tag_cap.txt")))      
    inputfile = os.path.abspath(os.path.join(file))
    print(inputfile)
    print(taggedfile_cap)
    subprocess.call([tagger_cap, inputfile, taggedfile_cap])
#    subprocess.call([tagger_nocap, inputfile, taggedfile_nocap])
#    return taggedfile_cap, taggedfile_nocap


def mergetag(pr, file, type_pr):
    if type_pr == 'Python_corp':
        if os.path.isdir(os.path.join('..', 'corpus', 'data', 'tag_aut', pr)) == False:
            os.mkdir(os.path.join('..', 'corpus', 'data', 'tag_aut', pr))
        p = os.path.join('..', 'corpus', 'data', 'work', pr, file)
        path_taggedfile = os.path.join('..', 'corpus', 'data', 'tag_aut', pr, file.replace('.txt', '_tag.txt'))
    file_cap = opencsv_as_list(p.replace('.txt', '_tag_cap.txt'))
    file_nocap = opencsv_as_list(p.replace('.txt', '_tag_nocap.txt'))
    counter = 0
    while counter < len(file_cap) - 4:
        if counter == 0:
            if file_cap[counter][1] != file_nocap[counter][1]:
                file_cap[counter][1] = file_nocap[counter][1]
                file_cap[counter][2] = file_nocap[counter][2]
        else:
            if file_cap[counter][1] != file_nocap[counter][1] and file_nocap[counter][1] == "XP" and \
                            file_nocap[counter - 1][1] != "FS" and file_nocap[counter - 1][1] != "QT" and \
                            file_nocap[counter - 1][1] != "DASH":
                file_cap[counter][1] = file_nocap[counter][1]
                file_cap[counter][2] = file_nocap[counter][2]
        counter += 1
    print_list_as_csv(file_cap, path_taggedfile)

def check_pos(pr, dict_pos, type_pr):

    if type_pr == 'Python_corp':
        pad = os.path.join('..', 'corpus', 'data', 'tag_corr_man', pr)
    p = opencsv_as_list(os.path.join('databases', dict_pos))
    dict_pos = {}
    for pos in p:
        dict_pos[pos[0]] = 1
    for file in os.listdir(pad):
        items = opencsv_as_list(os.path.join(pad, file))
        for item in items:
            if len(item) == 3 and item[1] not in dict_pos:
                print(file, item)

def rewrite_TT_as_text(file, path_project, correct): ##NOG HERWERKEN ALS WE DIT NODIG ZOUDEN HEBBEN!
    print(file)
    text_output = file + "\n\n"
    if correct == "yes":
        filename = os.path.join(path_project, "5_tagged_data", file.replace(".txt", "_tag_correct.txt"))
    if correct == "no":
        filename = os.path.join(path_project, "5_tagged_data", file.replace(".txt", "_tag.txt"))
    items = opencsv_as_list(filename)
    for item in items:
        if item[0] == "‡":
            text_output += "\n"
        elif len(item) == 3:
            text_output += "<p " + item[1] + ">" + item[0] + "<l " + item[2] + "> "
    h = codecs.open(os.path.join(path_project, "5_tagged_data", file.replace(".txt", "_tagged_text.txt")), 'w',
                    'utf-8-sig')
    h.write(text_output)
    h.close()


def analyze_sentences(project, source, dict_pos, type_pr): #veranderen alle path_project
    p = opencsv_as_list(os.path.join('databases', dict_pos))
    dict_pos = {}
    for i in p:
        if len(i) == 4:
            dict_pos[i[0]] = [i[1], i[2], i[3]]

    if type_pr == 'Python_corp':
        folder = os.path.join('..', 'corpus', 'data', source, project)
        if os.path.isdir(os.path.join('..', 'corpus', 'data', 'sent', project)) == False:
            os.mkdir(os.path.join('..', 'corpus', 'data', 'sent', project))
        pad_output = os.path.join('..', 'corpus', 'data', 'sent', project)
    for filename in os.listdir(folder):
        lijst123 = opencsv_as_list(os.path.join(folder, filename))
        lijst132 = []
        for lijn in lijst123:
            if len(lijn) == 3:
                if lijn[1] == 'FS':
                    lijn[1] = lijn[1].replace('FS', 'FS^$')
                newlijn = [lijn[0], lijn[2], lijn[1]]
                lijst132.append("\t".join(newlijn))
        joinlijst132 = "\r\n".join(lijst132)
        sentencesplit2 = []
        newsplit2 = []
        newsplit4 = []
        for element in joinlijst132.split("^$\r\n"):
            sentencesplit2.append(element)
        for element2 in sentencesplit2:
            element3 = element2.split("\r\n")
            newsplit2.append(element3)
        counter = 0
        while counter < len(newsplit2):
            newsplit3 = []
            for element4 in newsplit2[counter]:
                element5 = element4.split("\t")
                newsplit3.append(element5)
            newsplit4.append(list(newsplit3))
            counter += 1
        d_sent = {}        
        for index, sentence in enumerate(newsplit4):
            sent_tok = []
            sent_pos = []
            sent_lem = []
            counter2 = 0
            for item in sentence:
                if counter2 < len(sentence):
                    sent_tok.append(sentence[counter2][0])
                    sent_pos.append(sentence[counter2][2])
                    sent_lem.append(sentence[counter2][1])
                    counter2 += 1
            counter_words = counter_cont = counter_verbfin = counter_verbnonfin = 0
            for pos in sent_pos:
                if pos != 'FS^$':
                    if 'orto' not in dict_pos[pos]:
                        counter_words += 1
                    if 'content' in dict_pos[pos]:
                        counter_cont += 1
                    if 'verbfin' in dict_pos[pos]:
                        counter_verbfin += 1
                    if 'verbnonfin' in dict_pos[pos]:
                        counter_verbnonfin += 1
            d_sent[index] = {'tok': sent_tok, 'pos': sent_pos, 'lem': sent_lem, 'len': len(sentence), 'c_words': counter_words,
                            'c_cont': counter_cont, 'c_verbfin': counter_verbfin, 'c_verb': counter_verbfin+counter_verbnonfin}
            # tellen van categorieën pos
        print(filename)
        q = codecs.open(os.path.join(pad_output, filename.replace('_tag.txt', '_sent.json')), 'w', 'utf-8-sig')
        json.dump(d_sent, q)
            #q.close()

def index(project):
    pr = os.path.join('..', 'corpus', 'data', 'sent', project)
    d_index = {}
    for file in os.listdir(pr):
        g = codecs.open(os.path.join(pr, file), 'r', 'utf-8-sig')
        file = file.replace('_sent.json', '')
#       file = file.replace(project, '')
        d = json.load(g)
        for sent in d:
            for i, l in enumerate(d[sent]['lem']):
                j = d[sent]['pos'][i]
                if l not in d_index:
                    d_index[l] = {j : {file: {sent: [i]}}}
                elif j not in d_index[l]:
                    d_index[l][j] = {file: {sent: [i]}}
                elif file not in d_index[l][j]:
                    d_index[l][j][file] = {sent : [i]}
                elif sent not in d_index[l][j][file]:
                    d_index[l][j][file][sent] = [i]
                elif i not in d_index[l][j][file][sent]:
                    d_index[l][j][file][sent].append(i)
                if j.startswith('V'):
                    j = 'V'
                    if l not in d_index:
                        d_index[l] = {j : {file: {sent: [i]}}}
                    elif j not in d_index[l]:
                        d_index[l][j] = {file: {sent: [i]}}
                    elif file not in d_index[l][j]:
                        d_index[l][j][file] = {sent : [i]}
                    elif sent not in d_index[l][j][file]:
                        d_index[l][j][file][sent] = [i]
                    elif i not in d_index[l][j][file][sent]:
                        d_index[l][j][file][sent].append(i)

        print(file)
    g = codecs.open(os.path.join('..', 'corpus', 'metadata', 'index_lem','corp_index_'+project+'.json'), 'w', 'utf-8-sig')
    json.dump(d_index, g)
    g.close()

def percentile_20(array):
    array_no_hoax = []
    for freq in array:
        if freq > 1:
            array_no_hoax.append(freq)
    counters = [20,40,60,80]
    tresholds = []
    dict_values = {}
    for counter in counters:
        if array_no_hoax:
            treshold = numpy.percentile(array_no_hoax, counter)
            tresholds.append(treshold)
    for value in set(array):
        if value == 1:
            dict_values[value] = 0
        elif value < tresholds[0]:
            dict_values[value] = 1
        elif value >= tresholds[0] and value < tresholds[1]:
            dict_values[value] = 2
        elif value >= tresholds[1] and value < tresholds[2]:
            dict_values[value] = 3
        elif value >= tresholds[2] and value < tresholds[3]:
            dict_values[value] = 4
        elif value >= tresholds[3]:
            dict_values[value] = 5
    return dict_values

def count_parameters_sent_corp(project, files, type_pr):
    
    if type_pr == 'Python_corp':
        pad_in = os.path.join('..', 'corpus', 'data', 'sent', project)
        pad_out = os.path.join('..', 'output', 'stats', project)
        if os.path.isdir(pad_out) == False:
            os.mkdir(pad_out)
    g_all = 0
    h_all = 0
    i_all = 0
    j_all = 0
    k_all = 0
    n_s = 0
    d_freq = {}
    d_freq[project] = {}
    for file in files:
        print(file)
        g = 0
        h = 0
        i = 0
        j = 0
        k = 0
        file_open = codecs.open(os.path.join(pad_in, file), 'r', 'utf-8-sig')
        l_sent = json.load(file_open)

        file_open.close()
        code_file = file.replace('_sent.json', '')
        d_freq[code_file] = {}
        n_s += len(l_sent)
        for key, sentence in l_sent.items():
            # d_sent[index] = {'tok': sent_tok, 'pos': sent_pos, 'lem': sent_lem, 'len': len(sentence), 'c_words': counter_words,
            #                 'c_cont': counter_cont, 'c_verbfin': counter_verbfin, 'c_verb': counter_verbfin+counter_verbnonfin}
            g += int(sentence["len"])
            i += int(sentence["c_words"])
            if sentence["c_verbfin"] > 0:
                k += 1
                h += sentence["len"]
                j += sentence["c_words"]
        d_freq[code_file]['c_signs'] = g
        d_freq[code_file]['c_words'] = i
        d_freq[code_file]['c_sent'] = len(l_sent)
        d_freq[code_file]['c_sent_fin'] = k
        d_freq[code_file]['c_signs_mean_all'] = "{0:.2f}".format(g/len(l_sent))
        d_freq[code_file]['c_signs_mean_fin'] = "{0:.2f}".format(h/k)
        d_freq[code_file]['c_words_mean_all'] = "{0:.2f}".format(i/len(l_sent))
        d_freq[code_file]['c_words_mean_fin'] = "{0:.2f}".format(j/k)
        g_all += g
        h_all += h
        i_all += i
        j_all += j
        k_all += k
        for criterium in ['c_cont', 'c_verb', 'c_verbfin']:
            l = 0
            m = 0
            n = 0
            for key, sentence in l_sent.items():
                l += sentence[criterium]
            for key, sentence in l_sent.items():
                if sentence["c_verbfin"] > 0:
                    m += sentence[criterium]
                    n += 1
            d_freq[code_file][criterium+'_mean_all'] = "{0:.2f}".format(l/len(l_sent))
            d_freq[code_file][criterium+'_mean_fin'] = "{0:.2f}".format(m/n)
            d_freq[code_file][criterium] = l
    d_freq[project]['all_signs'] = g_all
    d_freq[project]['all_words'] = i_all
    d_freq[project]['n_sentences'] = n_s
    d_freq[project]['n_sentences_fin'] = k_all
    d_freq[project]['all_signs_mean_all'] = "{0:.2f}".format(g_all/n_s)
    d_freq[project]['all_signs_mean_fin'] = "{0:.2f}".format(h_all/k_all)
    d_freq[project]['all_words_mean_all'] = "{0:.2f}".format(i_all/n_s)
    d_freq[project]['all_words_mean_fin'] = "{0:.2f}".format(j_all/k_all)

    #   synthese += "mean_" + criterium + "\t\t" + str("{0:.2f}".format(g/len(list_allsentences))) + "\t\t" + str("{0:.2f}".format(h/i)) + "\n"
    g = codecs.open(os.path.join(pad_out, project+'_stats.json'), 'w', 'utf-8-sig')
    json.dump(d_freq, g)
    g.close()
    for k in d_freq:
        for l in d_freq[k]:
            print(k, l, d_freq[k][l])

def frequency_lema_pos(project, files, type_pr): #TO DO: POS V samentellen en ook frequentie opnemen, dictfrequenties gebruiken, en overzicht aanmaken
    print("start frequency pos lemma")

    if type_pr == 'Python_corp':
        pad_in = os.path.join('..', 'corpus', 'data', 'sent', project)
        pad_out = os.path.join('..', 'output', 'stats', project)
        if os.path.isdir(pad_out) == False:
            os.mkdir(pad_out)
    dict_freq_POS = {}
    dict_freq_LEM = {}
    dict_freq_NC = {}
    dict_freq_ADJ = {}
    dict_freq_ADJV = {}
    dict_freq_ADV = {}
    dict_freq_VERBS = {}
    dict_freq_XP = {}
    dict_freq_PE = {}
    for file in files:
        ## create dictionaries per file
        dict_freq_pos = {}
        dict_freq_lem = {}
        dict_freq_nc = {}
        dict_freq_adj = {}
        dict_freq_adjv = {}
        dict_freq_adv = {}
        dict_freq_verbs = {}
        dict_freq_xp = {}
        dict_freq_pe = {}
        ## open file
        file_open = codecs.open(os.path.join(pad_in, file), 'r', 'utf-8-sig')
        l_sent = json.load(file_open)
        file_open.close()
        code_file = file.replace('_sent.json', '')
        for key, sentence in l_sent.items():
            for pos in sentence['pos']:
                dict_count(dict_freq_pos, pos)
                dict_count(dict_freq_POS, pos)
            for i, lem in enumerate(sentence['lem']):
                dict_count(dict_freq_lem, lem)
                dict_count(dict_freq_LEM, lem)
                if sentence['pos'][i] == "NC":
                    dict_count(dict_freq_nc, lem)
                    dict_count(dict_freq_NC, lem)
                elif sentence['pos'][i] in ["ADJ"]:
                    dict_count(dict_freq_adj, lem)
                    dict_count(dict_freq_ADJ, lem)
                elif sentence['pos'][i] in ["ADJV"]:
                    dict_count(dict_freq_adjv, lem)
                    dict_count(dict_freq_ADJV, lem)
                elif sentence['pos'][i] in ["ADV"]:
                    dict_count(dict_freq_adv, lem)
                    dict_count(dict_freq_ADV, lem)
                elif sentence['pos'][i].startswith("V"):
                    dict_count(dict_freq_verbs, lem)
                    dict_count(dict_freq_VERBS, lem)
                elif sentence['pos'][i] == "XP":
                    dict_count(dict_freq_xp, lem)
                    dict_count(dict_freq_XP, lem)
                elif sentence['pos'][i] == "PE":
                    dict_count(dict_freq_pe, lem)
                    dict_count(dict_freq_PE, lem)       
        dict_dictionaries = {"XP": dict_freq_xp, "PE": dict_freq_pe, "ADV": dict_freq_adv, "NC": dict_freq_nc, "V": dict_freq_verbs, "POS": dict_freq_pos, "LEM": dict_freq_lem, "ADJ": dict_freq_adj, 'ADJV': dict_freq_adjv}
        for name, d in dict_dictionaries.items():
            d_new = {}
            freqs = []
            for lem_key, lem_value in d.items():
    #           print(lem_key, lem_value, lem_value[0])
                freqs.append(lem_value)
            pctil = percentile_20(freqs)
            for lem_key, lem_value in d.items():
                lem_value_list = {'freq': lem_value, 'pctil': pctil[lem_value]}
                d_new[lem_key] = lem_value_list
            dict_dictionaries[name] = d_new
        g = codecs.open(os.path.join(pad_out, file.replace('_sent.json', '_freq_lex.json')), 'w', 'utf-8-sig')
        json.dump(dict_dictionaries, g)
        g.close()
    dict_dictionaries2 = {"XP": dict_freq_XP, "PE": dict_freq_PE, "ADV": dict_freq_ADV, "NC": dict_freq_NC, "V": dict_freq_VERBS, "POS": dict_freq_POS, "LEM": dict_freq_LEM, "ADJ": dict_freq_ADJ, 'ADJV': dict_freq_ADJV}
    for name, d in dict_dictionaries2.items():
        d_new = {}
        freqs = []
        for lem_key, lem_value in d.items():
            freqs.append(lem_value)
        pctil = percentile_20(freqs)
        for lem_key, lem_value in d.items():
            lem_value_list = {'freq': lem_value, 'pctil': pctil[lem_value]}
            d_new[lem_key] = lem_value_list
        dict_dictionaries2[name] = d_new
    g = codecs.open(os.path.join(pad_out, project+'_freq_lex.json'), 'w', 'utf-8-sig')
    json.dump(dict_dictionaries2, g)
    g.close()
    for d in dict_dictionaries2:
        print(dict_dictionaries2[d])
        print('XXXXXXXXXXXXXXXXXX')

def voc_level_TWS(dict_level, project, files, type_pr):

    print("start voc_level_tws")
    if type_pr == 'Python_corp':
        pad_in = os.path.join('..', 'output', 'stats', project)
        pad_out = os.path.join('..', 'output', 'stats', project)
    if type_pr == 'Local_project':
        pad_in = os.path.join(project, 'metadata')
        pad_out = os.path.join(project, 'metadata')
    files.append(project+'_sent.json') ##checken of dit lukt om ook project aan te hangen
    h = codecs.open(dict_level, 'r', 'utf-8-sig')
    base_dict_level = json.load(h)
    h.close()
    for file in files:
        g = codecs.open(os.path.join(pad_in, file.replace('_sent.json', '_freq_lex.json')), 'r', 'utf-8-sig')
        lemmalist = json.load(g)
        g.close() 
        lemmalist2 = {}
        counter_total = 0
        counter_lemma = 0
        counter_basic = 0
        counter_intermediate = 0
        counter_new = 0
        for cat in ['XP', 'PE', 'LEM', 'POS']:
            lemmalist2[cat] = lemmalist[cat]
        for cat in ['ADJ', 'ADJV', 'ADV', 'V', 'NC']:
            for lemma, value in lemmalist[cat].items(): ##hier stond vroeger lemmalist[1:] ##hier is er wel nog een probleem met vormen die ambigu zijn: worden overschreven
                counter_total += value['freq']
                counter_lemma += 1
                if lemma in base_dict_level and base_dict_level[lemma] == "1":
                    lemmalist[cat][lemma]['lev'] = 1
                    print(lemmalist[cat][lemma])
                    counter_basic += value['freq']
                elif lemma in base_dict_level and base_dict_level[lemma] == "2":
                    lemmalist[cat][lemma]['lev'] = 2
                    counter_intermediate += value['freq']
                elif lemma not in base_dict_level:
                    lemmalist[cat][lemma]['lev'] = 0
                    counter_new += value['freq']
                else:
                    print("error known_new ", lemma)
            lemmalist2[cat] = lemmalist[cat]
        for cat in lemmalist2:
            print(lemmalist2[cat])
        g = codecs.open(os.path.join(pad_out, file.replace('_sent.json', '_freq_lex.json')), 'w', 'utf-8-sig')
        json.dump(lemmalist2, g)
        g.close() 

def voc_contrast(project, refcorps, type_pr):
    print("start voc_contrast")
    if type_pr == 'Python_corp':
        pad_in = os.path.join('..', 'output', 'stats', project)
        pad_out = os.path.join('..', 'output', 'stats', project)
    if type_pr == 'Local_project':
        pad_in = os.path.join(project, 'metadata')
        pad_out = os.path.join(project, 'metadata')
    g = codecs.open(os.path.join(pad_in, project+'_freq_lex.json'), 'r', 'utf-8-sig')
    d_lex = json.load(g)
    g.close()
    d_lex_new = {}
    if refcorps[0] != "empty":
        g = codecs.open(os.path.join('..', 'output', 'stats', refcorps[0], refcorps[0]+'_freq_lex.json'), 'r', 'utf-8-sig')
        d_lex_ref = json.load(g)
        g.close()

    for cat in d_lex:
        if cat not in ['NC', 'V', 'ADJ', 'ADJV', 'ADV']:
            d_lex_new[cat] = d_lex[cat]
        else:
            for lema, value in d_lex[cat].items():
                if lema in d_lex_ref[cat]:
                    d_lex[cat][lema]['freq_'+refcorps[0]] = d_lex_ref[cat][lema]['freq']
                    if d_lex[cat][lema]['pctil'] > 2:
                        if d_lex[cat][lema]['pctil'] - d_lex_ref[cat][lema]['pctil'] > 1:
                            d_lex[cat][lema]['dif_'+ refcorps[0]] = 'A'
                        else:
                            d_lex[cat][lema]['dif_'+ refcorps[0]] = 'C'
                    else:
                        if d_lex[cat][lema]['pctil'] - d_lex_ref[cat][lema]['pctil'] > 1:
                            d_lex[cat][lema]['dif_'+ refcorps[0]] = 'B'
                        else:
                            d_lex[cat][lema]['dif_'+ refcorps[0]] = 'D'
                else:
                    if d_lex[cat][lema]['pctil'] > 2:
                        d_lex[cat][lema]['dif_'+ refcorps[0]] = 'A'
                    elif d_lex[cat][lema]['pctil'] > 0:
                        d_lex[cat][lema]['dif_'+ refcorps[0]] = 'B'
                    else:
                        d_lex[cat][lema]['dif_'+ refcorps[0]] = 'D'
            d_lex_new[cat] = d_lex[cat]
    g = codecs.open(os.path.join(pad_in, project+'_freq_lex.json'), 'w', 'utf-8-sig')
    json.dump(d_lex_new, g)
    g.close()