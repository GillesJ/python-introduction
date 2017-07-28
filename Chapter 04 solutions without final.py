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
