"""two words are anagrams if you can rearrange the letters from one to spell the other. 
Write a function called is_anagram that takes two strings and returns True if they are anagrams."""

def is_anagram (string1, string2):
	if sorted(string1) == sorted(string2):
		return True

print(is_anagram('nails', 'snail'))