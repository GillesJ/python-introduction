#   this script only takes the content words of a text into account
#   for every input file the following documents are created:
#       -dictionary containing the content words as keys with its number of occurrences and its position on the SoNaR frequency list
#       - dictionary containing all the content words in the

import codecs
import os
import json
import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot

def only_content_words (filename_in,directory_in):

    """
    This function only works for texts pos tagged by the same pos tagger as LeTs Preprocessing tool.
    it only selects the pos tags that bare content information:
    WW (verbs), N (nouns), ADJ (adjectives), BW (adverbs) and SPEC (proper names) carry content
    In the folder "04contentwords" for every input file an output file is generated presenting all the content words
    filename_out and len(l_contentwords) are returned.
    """

    f_in = codecs.open(filename_in, "r", "utf-8") #read the file for which we want only the the content words
    text = f_in.readlines()# returns a string
    f_in.close()

    text_without_blanks = list(line.strip() for line in text if line != "\n")

    l_contentwords = []
    for line in text_without_blanks:
        token, pos, score = line.split(" ")

        if (pos.startswith("WW(") or pos.startswith("N(") or pos.startswith("ADJ(") or pos.startswith("BW(") or pos.startswith("SPEC(")):
            l_contentwords.append(token)

    output_directory = directory_in.replace("03POS", "04contentwords")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    f1 = filename_in.replace("03POS", "04contentwords")
    filename_out = f1.replace(".pos", "_content_words.txt")

    with open(filename_out, "w") as output_file:
        for token in l_contentwords:
            if token is not l_contentwords[-1]: # if it is the last word in the list, no need to add \n, then we can use the len of the list!
                output_file.write(token+"\n")
            else:
                output_file.write (token)


    return filename_out, len(l_contentwords)


def get_positions_SoNaR (filename_in, directory_in):
    """
    This function searches for every (content) word in a file (filename_in), its position on the SoNaR500 frequency list.
    It returns a dictionary "d_output" for every filename_in containing the word itself, its position on the SoNaR500
    frequency list and the number of occurrences of the word in this file
    Words present in the output that are not in the SoNaR500 list are stored in a separate list "l_token_not_SoNaR".
    d_output and l_token_not_SoNaR thus are generated for every filename in and written (dumped) to a json file.
    """
    f1_in=codecs.open (os.path.join ("data","FreqSONAR_combined.txt"), "r","utf-8")
    list_lines_sonar= f1_in.readlines () #this splits document into lines containing a string "occurences\tnumberofdocs\ttoken\n"
    f1_in.close()

    f2_in = codecs.open(filename_in, "r")
    text = f2_in.read()  # returns a string
    f2_in.close()

    d_SoNaR = {}   # dictionary : "token" = position on SoNaR frequency list

    for index,line in enumerate(list_lines_sonar):
        l_separate_items = line.strip().split("\t")
        token = l_separate_items[-1]  #only token
        d_SoNaR[token]= index-2  #the first token is on line 4

    #  generating a list/ dictionary with the number of occurrences and corresponding frequency ranking
    #  attention! words not occurring in frequency list --> append in other list "out of voc"

    d_output = {}    # dictionary: "token" = [position on SoNaR, occurrences]
    d_token_not_SoNaR= {}
    l_token_not_SoNaR=[]
    occurrences = 0

    words = text.split("\n")
    for token in words:
        token= token.lower() #tokens must be only content words
        if token not in d_output: # if this is the first occurrence of the word --> add to dictionary
            if token not in d_SoNaR: # if the word is not in the SoNaR frequency list --> add to d_token_not_SoNaR
                occurrences = 1
                d_token_not_SoNaR[token] =[occurrences]
                l_token_not_SoNaR.append(token)

            if token in d_SoNaR:
                occurrences = 1
                position = d_SoNaR.get(token)
                d_output[token]=[position, occurrences]

        else:
            if token in d_SoNaR:
                occurrences+= 1
                position = d_SoNaR.get(token)
                d_output[token]=[position, occurrences]

            if token not in d_SoNaR:
                occurrences+=1
                d_token_not_SoNaR[token] = [occurrences]

    output_directory_2= os.path.splitext(directory_in.replace("03POS", "05_output_dict"))[0]

    if not os.path.exists(output_directory_2):
        os.makedirs(output_directory_2)

    filename_base= os.path.basename(filename_in).replace("_content_words","_output_dict")
    filename_out=os.path.join(output_directory_2,filename_base)

    with open( filename_out, "w") as f:
        json.dump (d_output,f)
    with open (os.path.join (output_directory_2.replace("05_output_dict",""), "out_of_voc.txt"), "w") as f:
        for item in l_token_not_SoNaR:
            f.write("%s\n" % item)

    number_out_of_voc_words= len (d_token_not_SoNaR)
    d_output["number_out_of_voc_words"] = number_out_of_voc_words

    return d_output

def get_info_tokens (list_dictionaries, sum_token, input_directory):

    """
    the 'get_info_tokens' function gathers all information from the dictionaries previously created per file,
    generating a sort of master dictionary with all content words as keys and a tuple with [position, occurrences] as its values.
    based this 'master dictionary' it calculates:
    -# types
    -# tokens
    -TTR
    -# out of vocabulary words (not in Sonar)
    -% out of vocabulary words
    -sum of all positions (to measure the frequency)
    -average frequency of content words used

    it returns the values of the following variables: sum_type, typetokenratio, number_out_of_voc, percentage_out_of_voc

    it generates the following files:
    -'output_info.txt':text file presenting vor variance : the number of types, the number of tokens and the type token ratio and for frequency : the total sum of all the positions of each content word and the average position of a word in the output.
    -'out_of_voc.txt' : text file presenting all the content words in the output that are not in the SoNaR500 list on a separate line.
    --'only_positions.txt' : file containing a comma separated list of only the positions of every content word
    """

    d_master={}           #the complete dictionary containing the keys of all the file separate dictionaries
    d_all_keys_pos={}       # containing only the index and the positions

    #d_master =
    # , with their frequency position on sonar and their occurrences in all the input files.
    l_out_of_voc = []  # list containing the number of out of vocabulary words for each input file
    for dict in list_dictionaries:
        for token in dict:

            if token == "number_out_of_voc_words":
                nr_out_of_voc_words = dict["number_out_of_voc_words"]
                l_out_of_voc.append(nr_out_of_voc_words)
                continue

            list_values = dict.get(token)
            position = list_values[0]
            occurrences = list_values[1]
            if token not in d_master.keys():
                d_master[token]= [position, occurrences]
                d_all_keys_pos[token] = position
            else:
                d_master[token][1] += occurrences

    l_only_positions= list (d_all_keys_pos.values())
    total_frequencyscore= (sum(l_only_positions))


    with open(os.path.join(input_directory.replace("03POS", ""), "only_positions.txt"), "w") as f:
        json.dump(l_only_positions,f)

    with open (os.path.join (input_directory.replace("03POS",""), "d_master_output.txt"), "w") as f:
        for key in d_master:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in d_master.items()]


    sum_type=len(d_master)-1
    typetokenratio= sum_type/sum_token
    number_out_of_voc = sum(l_out_of_voc)
    percentage_out_of_voc=number_out_of_voc/sum_token
    total_in_voc_words = sum_token - number_out_of_voc
    average_frequency= total_frequencyscore/total_in_voc_words

    with open (os.path.join(input_directory.replace("03POS",""), "output_info.txt"), "w") as f:
        f.write("Variance of output:" + "\n\n"+"sum type = " + str(sum_type) + "\n" + "sum token = " + str(sum_token) +"\n" + "TTR = " + str(typetokenratio)+"\n\n" + "sum_all_positions = " + str(total_frequencyscore) + "\n" + "average frequency = " + str(average_frequency))


    return sum_type, typetokenratio, number_out_of_voc, percentage_out_of_voc

def visualize (input_directory):

    """
    the visualize function reads data  (in this case a list of positions) from a json file and plots them in a histogram.
    the histogram is saved as a png in the correct MT subfolder (NMT/ SMT/ RBMT)
    """
    file_in= (os.path.join(input_directory.replace("03POS", ""), "only_positions.txt"))

    with open(file_in, "r") as f:
        x=json.load(f)

    plt.hist(x, histtype='stepfilled', bins=1000) # maybe better to plot in log10(x)to have a clearer view
    plt.xlim(xmin=0, xmax=150000)
    plt.title("the frequency of words used in the ouput")
    plt.xlabel("position on SoNaR500")
    plt.ylabel("log 10 # content words")
    plt.yscale("log")
    plt.savefig(os.path.join(input_directory.replace("03POS", ""), "hist.png"))
    plt.clf()


def process (input_directory):

    """
    the process function combines all functions and applies them for every file in a directory (input_directory)

    """
    l_files_in = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

    l_all_dicts = []
    l_lengths=[]
    for file in l_files_in:
        filename_content_words,len_content_words = only_content_words(file,input_directory)
        l_lengths.append(len_content_words)
        l_all_dicts.append(get_positions_SoNaR(filename_content_words,input_directory))

    get_info_tokens(l_all_dicts, sum(l_lengths), input_directory)
    visualize(input_directory)


#input_directory =  os.path.relpath ("data/Test/03POS")
#process(input_directory)
input_directory =  os.path.relpath ("data/NMT/03POS")
process(input_directory)
input_directory =  os.path.relpath ("data/SMT/03POS")
process(input_directory)
input_directory =   ("data/RBMT/03POS")
process(input_directory)

"""A combined plot of the output of the three engines is created below:"""

with open (os.path.join("data","NMT/only_positions.txt"), "r")as f1:
    l_nmt_values=json.load(f1)
with open (os.path.join("data","SMT/only_positions.txt"), "r")as f2:
    l_smt_values=json.load(f2)
with open (os.path.join("data","RBMT/only_positions.txt"), "r")as f3:
    l_rbmt_values=json.load(f3)

a=l_nmt_values
b=l_smt_values
c=l_rbmt_values

#bins = np.linspace(0, 1000000, 1000)
bins= [x for x in range(0,150000,1000)]
plt.xlim(xmin=0, xmax=150000)
plt.title("the frequency of words used in the ouput")
pyplot.hist(a, bins,color='b', label='nmt')
pyplot.hist(b,bins,color = 'g', label='smt')
pyplot.hist (c, bins, color = 'r', label='rbmt')


plt.xlabel("position on SoNaR500")
plt.ylabel(" # content words")
plt.yscale("log")
pyplot.legend(loc='upper right')
plt.savefig(os.path.join("data","comparison_histogram.png"))
plt.clf()










