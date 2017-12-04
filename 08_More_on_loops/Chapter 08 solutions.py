## DIY 1
import codecs
f = codecs.open("data/austen-emma-excerpt.txt", "r", "utf-8")
lines = f.readlines()
for index, line in enumerate(lines):
    print(index+1, line.strip())

## DIY 2
letters1 = list("abcdefghijklm")
letters2 = list("nopqrstuvwxyz")
rot13 = {}

## Your code goes here
for l1, l2 in zip(letters1, letters2):
    rot13[l1] = l2
    rot13[l2] = l1

## Test
message = "pbatenghyngvbaf, lbh oebxr gur pbqr!"
decrypted_message = "".join(rot13.get(l, l) for l in message)
    # FYI: the .get dictionary method looks up the first argument as a key, and returns the second argument in case of a KeyError
print(decrypted_message)

## DIY 3
lowercased_words2 = [word.lower() for word in words]
consonants2 = [letter for letter in alphabet if letter not in "aeiouy"]
laughter2 = {i: "ha"*i for i in range(1, 10)}

