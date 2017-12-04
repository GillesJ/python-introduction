  def is_anagram(word1, word2):
  	word1 = list(word1.upper())
  	word2 = list(word2.upper())
  	word1.sort()
  	word2.sort()
  	if word1 == word2:
  		return True
  	else:
  		return False

print(is_anagram('listen' , 'silent' ))
  	

