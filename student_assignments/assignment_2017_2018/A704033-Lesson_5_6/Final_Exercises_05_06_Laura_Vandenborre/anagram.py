def is_anagram(word_1, word_2):
	if len(word_1) != len(word_2):
		return False
	for letter in word_1:
		if letter not in word_2:
			return False
	for letter in word_2:
		if letter not in word_1:
			return False
	else:
		return True
    
print(is_anagram("dog", "cat"))
print(is_anagram("angel", "glean"))