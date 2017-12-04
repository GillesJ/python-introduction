import codecs
from string import punctuation

"""
Ideally, I would group read and import, case and punctuation, and freq_dict generation as three main functions and call (shorter) hapax functions afterwards.
However, to anticipate difficulties in parsing and splitting strings in foreign languages, I have created shorter modules in this assignment to re-use later.
"""

def open_file(filename):
	print("reading file")
	file = codecs.open(filename,"r","utf-8")
	raw_string = file.read()
	file.close()
	return raw_string

def lower_list(raw_string):
	print("removing cases")
	punctuated_list = raw_string.lower().split() 
	return punctuated_list

def remove_punctuation(punctuated_list):
	print("removing punctuation")
	counter = -1
	clean_list = []
	for item in punctuated_list:
		counter += 1
		punctuated_list[counter] = item.strip(punctuation)
	counter = -1
	return punctuated_list

def create_dict(clean_list):
	print("calculating frequencies")
	frequency_dict = {}
	for word in clean_list:
		if word not in frequency_dict:     
			frequency_dict[word] = clean_list.count(word)
		else:
			pass
	return frequency_dict

""" Included for later reference, just in case...
from collections import OrderedDict

def sort_by_decreasing_value(frequency_dict):
	print("sorting")
	sorted_list = OrderedDict(sorted(frequency_dict.items(), key=lambda t: t[1], reverse=True))
	return sorted_dict

def sort_by_increasing_value(frequency_dict):
	print("sorting")
	sorted_list = OrderedDict(sorted(frequency_dict.items(), key=lambda t: t[1], reverse=False))
	return sorted_dict
"""

def hapax_legomena(frequency_dict):
	legomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 1:
			legomena_list.append(item)
		else:
			pass
	return legomena_list

def vertical_export_to_filename(filename):
	export = codecs.open(filename,"w","utf-8")
	for item in output:
		export.write(item+"\r\n")
	export.close()


def legomena(filename):
	print("FINDING LEGOMENA")
	raw_string = open_file(filename)
	punctuated_list = lower_list(raw_string)
	clean_list = remove_punctuation(punctuated_list)
	frequency_dict = create_dict(clean_list)
	legomena_list = hapax_legomena(frequency_dict)
	return legomena_list

#input
filename = "Autobiography of Benjamin Franklin.txt"

#function
output = legomena(filename)

#output
output_file = "hapax_legomena.txt"
vertical_export_to_filename(output_file)


print("Results successfully exported to",output_file)
print("I had to export to a file, because Sublime Text refused to print certain characters...")
