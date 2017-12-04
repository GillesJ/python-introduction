#!/usr/bin/env/ python

### 3 solutions, each relying on a list of sorted letters, from long to short
def anagram1(word1, word2):
	word1_letters_in_order = sorted(list(word1)) # cast the string as a list of characters and sort it
	word2_letters_in_order = sorted(list(word2))
	if word1_letters_in_order == word2_letters_in_order:
		return True
	else:
		return False

def anagram2(word1, word2):
	if sorted(word1) == sorted(word2): # calling sorted on a string automatically casts it as a list
		return True
	else:
		return False

def anagram3(word1, word2):
	return sorted(word1) == sorted(word2) # An equivalence test with == already produces a Boolean

print(anagram1("silent", "quiet"))
print(anagram1("silent", "listen"))
print(anagram2("silent", "quiet"))
print(anagram2("silent", "listen"))
print(anagram3("silent", "quiet"))
print(anagram3("silent", "listen"))