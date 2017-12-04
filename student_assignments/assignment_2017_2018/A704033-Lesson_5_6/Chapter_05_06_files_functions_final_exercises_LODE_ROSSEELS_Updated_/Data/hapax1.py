import codecs
import os
from string import punctuation

def legomena(filename):
	print("reading file")
	file = codecs.open(filename,"r","utf-8")
	raw_string = file.read()
	file.close()
	print("removing cases")
	punctuated_list = raw_string.lower().split() 
	print("removing punctuation")
	clean_list = []
	for item in punctuated_list:
		clean_list.append(item.strip(punctuation))
	print("calculating frequencies")
	frequency_dict = {}
	for word in clean_list:
		if word not in frequency_dict:     
			frequency_dict[word] = clean_list.count(word)
	print("extracting legomena")
	legomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 1:
			legomena_list.append(item)
	return legomena_list

#input
filename = "Autobiography of Benjamin Franklin.txt"

#output
output = legomena(filename)
outputname = " - hapax legomena"


#export
export_filename = os.path.splitext(filename)
export_filename = export_filename[0]+outputname+str(export_filename[1])
export = codecs.open(export_filename,"w","utf-8")
for item in output:
	export.write(item+"\r\n")
export.close()
print("Results successfully exported to",export_filename)


print("NOTE: I had to export to a file, because Sublime Text refused to print certain characters...")
