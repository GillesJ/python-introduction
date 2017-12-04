import requests
import bs4
import codecs
import os

os.mkdir("output")

def create_dict(filename):
    f = codecs.open(filename, "r", "utf8")
    words = f.readlines()
    f.close()
    wc = {} #contains the words as keys and the word class as values.
    for word in words:
        word = "".join(word.split("\r\n"))
        word = word.split("\t")
        wc[word[0]] = word[1]
    return wc
    #For the synonyms and antonyms, it is not necessary to make three dicitionary (which is the case for the translations),
    #since wordreference apparently does not make any difference between word classes.

def find_syns_and_ants(filename):
    wc = create_dict(filename)
    dict_syn = {}
    dict_ant = {}
    for word in wc.keys():
        r = requests.get('http://www.wordreference.com/sinonimos/' + word)
        html = r.text
        soup = bs4.BeautifulSoup(html, "lxml")
        p = soup.p.text
        if p == "No se ha encontrado sinónimos para " + "'" + word + "'.":
            dict_ant[word] = ["No antonyms on wordreference.com"]
            dict_syn[word] = ["No synonyms on wordreference.com"]
        else:
            for article in soup.find_all("div", {"id": "article"}):
                lemma = article.find("h3").text
                if lemma == word:
                    for div in article.find("div", {"class": "trans clickable"}):
                        #defining antonyms
                        ants = []
                        for antonyms in div.find_all("ul"):
                            ant = " ".join(antonyms.text.split(", "))
                            ant = ant.split()
                            ant.remove("Antónimos:")
                            ants.append(ant)
                        if ants:
                            dict_ant [word] = ants
                        else:
                            dict_ant [word] = ["No antonyms on wordreference.com"]
                        #defining synonyms
                        syns = []
                        for synonyms in div.find_all("li"):
                            syn = synonyms.text.split()
                            if "Antónimos:" in syn:
                                syn.remove("Antónimos:")
                            syn = (" ".join(syn)).split(", ")
                            if syn not in dict_ant[word]: #The syn list contains both the synonyms and the antonyms. However, by creating the anontyms list first,
                                syns.append(syn)          #words that are not in the antonyms list are appended to the synonyms list.
                        if syns:
                            dict_syn [word] = syns
                        else:
                            dict_syn [word] = ["No synonyms on wordreference.com"]
                else:
                    dict_syn [word] = ["No synonyms on wordreference.com"]
                    dict_ant [word] = ["No antonyms on wordreference.com"]
    return wc, dict_syn, dict_ant
        

def syns_and_ants(filename):
    wc, dict_syn, dict_ant = find_syns_and_ants(filename)
    f_syn = codecs.open("output/synonyms.txt", "w", "utf8")
    f_ant = codecs.open("output/antonyms.txt", "w", "utf8")
    for word in dict_syn:
        if dict_syn[word] == ["No synonyms on wordreference.com"]:
            synoniemen = " ".join(dict_syn[word])
            lemma_syn = word + "\t" + wc[word] + "\t" + synoniemen + "\n"
        else:
            lijst = []
            for li in dict_syn[word]:
                lijst.append(", ".join(li))
            synoniemen = "\n\t\t".join(lijst) #Two tabs are added, because that way, the synonyms are displayed under each other, instead of under the word class. (not in Notepad++, but when the content is copied to a word file)
            lemma_syn = word + "\t" + wc[word] + "\t" + synoniemen + "\n"    
        f_syn.write(lemma_syn)
    f_syn.close()
    for word in dict_ant:
        if dict_ant[word] == ["No antonyms on wordreference.com"]:
            antoniemen = " ".join(dict_ant[word])
            lemma_ant = word + "\t" + wc[word] + "\t" + antoniemen + "\n"
        else:
            lijst = []
            for li in dict_ant[word]:
                lijst.append(", ".join(li))
            antoniemen = "\n\t\t".join(lijst)
            lemma_ant = word + "\t" + wc[word] + "\t" + antoniemen + "\n"
        f_ant.write(lemma_ant)
    f_ant.close()
    print("Such fun! Synonyms and antonyms have been found ;)")