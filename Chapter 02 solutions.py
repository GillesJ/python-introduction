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

### FINAL EXERCISES
### Ex. 1
sentence1 = "Brad and Angelina kick the bucket"
sentence2 = "Bonny and Clyde are really famous"
s1_splitted = sentence1.split()
s2_splitted = sentence2.split()

sentence3 = s1_splitted[:3] + s2_splitted[-3:]
sentence3 = " ".join(sentence3)
sentence4 = s2_splitted[:3] + s1_splitted[-3:]
sentence4 = "+".join(sentence4)
print(sentence3)
print(sentence4)
print(sentence4[int(len(sentence4)/2)])

### Ex. 2
lookup = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
          'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
          'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
          's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
          'x':'x-ray', 'y':'yankee', 'z':'zulu'} # Don't change this line
lookup["k"] = "kilo"
lookup["l"] = "lima"
lookup["m"] = "mike"
msg = []
msg.append(lookup["m"])
msg.append(lookup["a"])
msg.append(lookup["r"])
msg.append(lookup["v"])
msg.append(lookup["e"])
msg.append(lookup["l"])
msg.append(lookup["l"])
msg.append(lookup["o"])
msg.append(lookup["u"])
msg.append(lookup["s"])
with_comma = ",".join(msg)
print(with_comma)

### Ex. 3
code_words = list(lookup.values())
print(code_words)
code_words.sort()
print(code_words)
code_words.remove("victor")
code_words.remove("india")
code_words.remove("papa")
print(code_words)
code_words.append("pigeon")
code_words.append("patato")
print(code_words)
single_string = ";".join(code_words)
print(single_string)
