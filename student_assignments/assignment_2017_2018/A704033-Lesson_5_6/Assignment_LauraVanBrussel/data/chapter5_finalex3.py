#Ex. 3: Write a program that takes a text file (e.g. filename.txt) and creates a new text file (e.g. filename_numbered.txt)
#  in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file),
#  i.e. prepend the number and a space to each line.

def numbered_lines(filename_in): #this function generates a new text file ("filename_numbered.txt") with all the lines preceded by the line number
    import os
    base = os.path.basename(filename_in)
    base_out = (os.path.splitext(base)[0]) + "_numbered" + os.path.splitext(base)[1]
    filename_out= os.path._getfullpathname(base_out)

    filename_in_pythonposition = os.path._getfullpathname(base)
    print(filename_in_pythonposition)
    print(filename_out)



    with open(filename_in,'r') as program:
        l_lines = program.readlines()

    with open(filename_out, 'w') as program:
        for (number, line) in enumerate(l_lines):
            program.write('%d  %s' % (number + 1, line))



#filename_in = "C:/Users/lvbrusse/Documents/doctoral schools/Python/final_excercises_6/data/ThePictureOfDorianGray.txt"
filename_in="ThePictureOfDorianGray.txt"



#filename_out="C:/Users/lvbrusse/Documents/doctoral schools/Python/final_excercises_6/data/ThePictureOfDorianGray_numbered.txt"
numbered_lines(filename_in)


