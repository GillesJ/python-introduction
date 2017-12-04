import codecs
from string import punctuation

def legomena(filename):
	print("reading file")
	file = codecs.open(filename,"r","utf-8")
	raw_string = file.read()
	file.close()
	print("removing cases")
	punctuated_list = raw_string.lower().split() 
	print("removing punctuation")
	counter = -1
	clean_list = []
	for item in punctuated_list:
		counter += 1
		punctuated_list[counter] = item.strip(punctuation)
	counter = -1
	print("calculating frequencies")
	frequency_dict = {}
	for word in punctuated_list:
		if word not in frequency_dict:     
			frequency_dict[word] = punctuated_list.count(word)
		else:
			pass
	print("extracting legomena")
	legomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 1:
			legomena_list.append(item)
		else:
			pass
	return legomena_list

#input
filename = "Autobiography of Benjamin Franklin.txt"

#output
output = legomena(filename)
export_filename = "hapax_legomena.txt"


#export
export = codecs.open(export_filename,"w","utf-8")
for item in output:
	export.write(item+"\r\n")
export.close()

print("Results successfully exported to",export_filename)
print("I had to export to a file, because Sublime Text refused to print certain characters...")
print("UnicodeEncodeError: 'charmap' codec can't encode character _____ in position 0: character maps to <undefined>")
