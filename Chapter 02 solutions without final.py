### Oneliner
print(", ".join(['banana', 'pear', 'apple']))

### Remove vowels
text = "Research has shown that it is often still possible to understand text even if all vowels are removed"
text = text.replace("a", "")
text = text.replace("e", "")
text = text.replace("i", "")
text = text.replace("o", "")
text = text.replace("u", "")
text = text.replace("y", "") # Depending on whether you consider this a vowel
print(text)

# Or a shorter version:
print(text.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("y", ""))

###
my_sentence = "I came up with a sentence"
my_words = my_sentence.split()
print(my_words)
print(len(sentence))
print(len(words))

### Lists
first_word = words[0]
fifth_word = words[4]
last_word = words[-1]
penultimate_word = words[-2]
word_slice = words[4:10]
tv_series = words[8:]

### Good reads list
good_reads.append("1984")
good_reads.append("There And Back Again")
good_reads[1] = "The Shining"
print(good_reads)

###
good_reads[0].append(1813) # Append date of publication to Pride and Prejudice entry
good_reads[1].append(1962) # Append date of publication to A Clockwork Orange entry
good_reads.append(["There and Back Again", 6, 1937]) # Append new entry
print(good_reads[0][1])
print(good_reads[2][2])

### Good reads dictionary
# good_reads = {} # In case you want to start with an empty dictionary
good_reads["There and Back Again"] = 6
print(good_reads["There and Back Again"])

