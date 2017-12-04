def is_anagram(string1, string2):
	anagram = True
	# anagrams are always equal in length -> it does not matter where you start counting
	if len(string1) != len(string2):
		anagram = False
	for char in string1:
		if string1.count(char) == string2.count(char):
			pass
		else:
			anagram = False 
	return anagram


print(is_anagram("unidentifiably", "undefinability"))

