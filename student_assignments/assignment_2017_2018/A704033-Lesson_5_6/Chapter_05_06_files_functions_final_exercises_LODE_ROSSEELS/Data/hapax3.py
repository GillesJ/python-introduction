import codecs
from string import punctuation


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


def hapax_dislegomena(frequency_dict):
	dislegomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 2:
			dislegomena_list.append(item)
		else:
			pass
	return dislegomena_list

def hapax_trilegomena(frequency_dict):
	trilegomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 3:
			trilegomena_list.append(item)
		else:
			pass
	return trilegomena_list

def vertical_export_to_filename(output, filename):
	print("exporting data")
	export = codecs.open(filename,"w","utf-8")
	for item in output:
		export.write(item+"\r\n")
	export.close()


#note: I have created 3 full functions, and am aware that if all three are needed, It would be better to have one freq_dict generation and three filters.
#I chose to write 3 standalone functions for the sake of practice, and because the functions don't take too long to compute anyways.

def legomena(filename):
	print("FINDING LEGOMENA")
	raw_string = open_file(filename)
	punctuated_list = lower_list(raw_string)
	clean_list = remove_punctuation(punctuated_list)
	frequency_dict = create_dict(clean_list)
	legomena_list = hapax_legomena(frequency_dict)
	return legomena_list

def dislegomena(filename):
	print("FINDING DISLEGOMENA")
	raw_string = open_file(filename)
	punctuated_list = lower_list(raw_string)
	clean_list = remove_punctuation(punctuated_list)
	frequency_dict = create_dict(clean_list)
	dislegomena_list = hapax_dislegomena(frequency_dict)
	return dislegomena_list

def trilegomena(filename):
	print("FINDING TRILEGOMENA")
	raw_string = open_file(filename)
	punctuated_list = lower_list(raw_string)
	clean_list = remove_punctuation(punctuated_list)
	frequency_dict = create_dict(clean_list)
	trilegomena_list = hapax_trilegomena(frequency_dict)
	return trilegomena_list



filename = "Autobiography of Benjamin Franklin.txt"



output_file = "hapax_legomena.txt"
vertical_export_to_filename(legomena(filename), output_file)

output_file2 = "hapax_dislegomena.txt"
vertical_export_to_filename(dislegomena(filename), output_file2)

output_file3 = "hapax_trilegomena.txt"
vertical_export_to_filename(trilegomena(filename),output_file3)


print("Results successfully exported as"+output_file+", "+output_file2+","+output_file3)
