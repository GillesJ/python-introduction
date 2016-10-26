### DIY 1
colors = ["yellow", "red", "green", "blue", "purple"]
for color in colors:
    print(len(color))

colors = ["yellow", "red", "green", "blue", "purple"]
colors_with_r = []
for color in colors:
    if "r" in color:
        colors_with_r.append(color)
print(colors_with_r)

### DIY 2
frequency_dictionary = {"Beg": 1, "Goddard's": 1, "I": 3, "them": 2, "absent": 1, "already": 1,
                          "alteration": 1, "amazement": 2, "appeared": 1, "apprehensively": 1, 
                          "associations": 1, 'clever': 1, 'clock': 1, 'composedly': 1, 
                          'deeply': 7, 'do': 7, 'encouragement': 1, 'entrapped': 1,
                          'expressed': 1, 'flatterers': 1, 'following': 12, 'gone': 9, 
                          'happening': 4, 'hero': 2, 'housekeeper': 1, 'ingratitude': 1, 
                          'like': 1, 'marriage': 15, 'not': 25, 'opportunities': 1,
                          'outgrown': 1, 'playfully': 2, 'remain': 1, 'required': 2, 
                          'ripening': 1, 'slippery': 1, 'touch': 1, 'twenty-five': 1,
                          'ungracious': 2, 'unwell': 1, 'verses': 1, 'yards': 5}
number_of_as = 0
print(number_of_as != 0)

# insert your code here
for word in frequency_dictionary: # For every word in our dictionary, do this:
    word_a_count = word.count("a") # Get the number of as in this word
    word_frequency = frequency_dictionary[word] # Look up this word's frequency in the dictionary
    number_of_as_because_of_this_word = word_a_count * word_frequency # Multiply the two
    number_of_as += number_of_as_because_of_this_word # Add this count to the total

# if your code is correct, the following line should print True!
print(number_of_as == 63)

### DIY 3
words = ['bicycle', 'radar', 'origin', 'tie', 'level', 'poop', 'solar', 'nun']
for word in sorted(words):
    if word == "".join(reversed(word)):
        print(word)

### Extra brownie points
text = "I just live for desserts , I really love them . My dog does too . I saw he ate mine . I was very stressed because of that . If dogs steal desserts God can't be real , for it is pure evil ." 
lowercased_text = text.lower()
words = lowercased_text.split(" ")
words = list(set(words)) # So that we don't have duplicate words anymore

for word in words:
    if len(word) > 1:
        reversed_word = "".join(reversed(word))
        if reversed_word in words:
            print(word, reversed_word)

### DIY 4
numbers = [1, 2, 3, 4, 5]
print(sum(numbers)/len(numbers))

### Final exercises
## Ex. 1
sentence = "Si six scies scient six cyprès , six cent six scies scient six cent six cyprès ."
words = sentence.lower().split() # Lowercase and split along whitespace
freq_dict = {}
for word in words:
    if word not in freq_dict: # If the word is not in the dictionary yet:
        freq_dict[word] = 1   # we need to make a new entry and initialize its count to 1
    else:                     # If the word already exists:
        freq_dict[word] += 1  # we need to update its count with 1
print(freq_dict)

### Alternative solution
freq_dict = {}
for word in words:
    if word not in freq_dict: # If the word is not in the dictionary yet:
        freq_dict[word] = 0   # we make a new entry and initialize its count to 0 
    freq_dict[word] += 1      # and then we update the count with one, regardless of whether the word was in the dict
print(freq_dict)

## Ex. 2
lengthy_word = "supercalifragilisticexpialidocious"
length = 0
for letter in lengthy_word:
    length += 1
print(length)

## Ex. 3
char_freqs = {}
for char in lengthy_word:
    if char in char_freqs:
        char_freqs[char] += 1
    else:
        char_freqs[char] = 1
print(char_freqs)

## Ex. 4
histogram = [4, 9, 7, 2, 16, 8, 3]
for value in histogram:
    print("+"*value)

## Ex. 5
# bottles of beer
counter = 99
while counter > 0:
    if counter == 1:
        print(str(counter), "bottle of beer on the wall,", str(counter), "bottle of beer. Take one down, pass it around,", str(counter-1), "bottles of beer on the wall.")
    elif counter == 2:
        print(str(counter), "bottles of beer on the wall,", str(counter), "bottles of beer. Take one down, pass it around,", str(counter-1), "bottle of beer on the wall.")
    else:
        print(str(counter), "bottles of beer on the wall,", str(counter), "bottles of beer. Take one down, pass it around,", str(counter-1), "bottles of beer on the wall.")
    counter -= 1

## Ex. 6
infinitive = "eat"
if infinitive.endswith("y"):
    print(infinitive[:-1] + "ies")
elif infinitive[-1] in ["o", "s", "x", "z"]:
    print(infinitive + "es")
elif infinitive[-2:] in ["ch", "sh"]:
    print(infinitive + "es")
else:
    print(infinitive + "s")

## Ex. 7
alphabet = list("abcdefghijklmnopqrstuvwxyz")
rot13_dict = {}
for letter in alphabet[:13]:
    index_plus_13 = alphabet.index(letter) + 13
    corresponding_letter = alphabet[index_plus_13]
    rot13_dict[letter] = corresponding_letter
for letter in alphabet[13:]:
    index_minus_13 = alphabet.index(letter) - 13
    corresponding_letter = alphabet[index_minus_13]
    rot13_dict[letter] = corresponding_letter

# Alternative solution
rot13_dict = {}
for letter in alphabet:
    letter_index = alphabet.index(letter)
    if letter_index < 13:
        corresponding_letter = alphabet[letter_index+13]
    else:
        corresponding_letter = alphabet[letter_index-13]
    rot13_dict[letter] = corresponding_letter
    
secret_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
decoded_secret_message = []
for letter in secret_message.lower():
    if letter in rot13_dict:
        decoded_secret_message.append(rot13_dict[letter])
    else:
        decoded_secret_message.append(letter)
print("".join(decoded_secret_message))
