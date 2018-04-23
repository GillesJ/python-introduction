#from bilingual text --> only copy NL part and make new document


import codecs
import os
import os.path


def onlyNL (filename_in,input_directory):

    f_in=codecs.open(filename_in, "r")
    all_lines=f_in.readlines()
    l_no_blank_lines= list(line for line in all_lines if line != "\n")

    f_in.close()

    base = os.path.basename(filename_in)

    base_out = (os.path.splitext(base)[0].replace("merged.merged.en-nl", "_NL-output").replace (".Google.merged.en-nl", ".SMT_NL-output").replace(".merged.en-nl", "_NL-output"))  + os.path.splitext(base)[1] # best nog aanpassen
    print (base_out)
    filename_out = os.path._getfullpathname(base_out)
    #print (filename_out)

    NL_lines = []

    line_nr = 0
    for line in l_no_blank_lines:
        line_nr += 1
        if (line_nr % 2 == 0):
            NL_lines.append(line)

    output_directory = (input_directory).replace("00Bilingual", "01NL_output")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(os.path.join(output_directory, filename_out), "w") as output_file:
        print (output_directory)
        for line in NL_lines:
            output_file.write(line)

def process_bilinguals (input_directory):

    #input_directory= os.path.relpath("C:/Users/lvbrusse/PycharmProjects/big_assignment_Language_Processing/data/00Bilingual/testNMT")
    l_files_in = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

    for file in l_files_in:
        onlyNL(file, input_directory)

input_directory= os.path.relpath("C:/Users/lvbrusse/PycharmProjects/big_assignment_Language_Processing/data/NMT/00Bilingual")
process_bilinguals (input_directory)
input_directory=os.path.relpath("C:/Users/lvbrusse/PycharmProjects/big_assignment_Language_Processing/data/SMT/00Bilingual")
process_bilinguals (input_directory)
input_directory=os.path.relpath("C:/Users/lvbrusse/PycharmProjects/big_assignment_Language_Processing/data/RBMT/00Bilingual")
process_bilinguals (input_directory)