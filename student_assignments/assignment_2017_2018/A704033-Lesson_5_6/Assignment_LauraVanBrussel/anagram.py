# two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(string1, string2):
    string1= string1.lower()
    string2= string2.lower()
    if  len(string1)==len(string2):
        for letter in string1:
            if letter in string2:
                string2=string2.replace(letter, " ")

            else:
                return False
        return True




string1= "Rosso"
string2= "Rooso"


result=is_anagram(string1,string2)
print(result)





