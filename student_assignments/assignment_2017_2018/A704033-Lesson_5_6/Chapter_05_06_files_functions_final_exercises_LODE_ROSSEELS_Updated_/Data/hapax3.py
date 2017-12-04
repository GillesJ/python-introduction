import codecs
import os
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
	clean_list = []
	for item in punctuated_list:
		clean_list.append(item.strip(punctuation))
	return clean_list

def create_dict(clean_list):
	print("calculating frequencies")
	frequency_dict = {}
	for word in clean_list:
		if word not in frequency_dict:     
			frequency_dict[word] = clean_list.count(word)
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
	return legomena_list


def hapax_dislegomena(frequency_dict):
	dislegomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 2:
			dislegomena_list.append(item)
	return dislegomena_list

def hapax_trilegomena(frequency_dict):
	trilegomena_list = []	
	for item in frequency_dict:
		if frequency_dict[item] == 3:
			trilegomena_list.append(item)
	return trilegomena_list

def vertical_export_to_filename(filename,output,outputname):
	export_filename = os.path.splitext(filename)
	export_filename = export_filename[0]+outputname+str(export_filename[1])
	export = codecs.open(export_filename,"w","utf-8")
	for item in output:
		export.write(item+"\r\n")
	export.close()
	print("Results successfully exported to",export_filename)

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

#note: I have created 3 full functions, and am aware that if all three are needed, It would be better to have one freq_dict generation and three filters.
#I chose to write 3 standalone functions for the sake of practice, and because the functions don't take too long to compute anyways.

outputname = " - hapax legomena"
vertical_export_to_filename(filename,legomena(filename),outputname)

outputname = " - hapax dislegomena"
vertical_export_to_filename(filename,dislegomena(filename),outputname)

outputname = " - hapax trilegomena"
vertical_export_to_filename(filename,trilegomena(filename),outputname)


print("NOTE: I had to export to a file, because Sublime Text refused to print certain characters...")
