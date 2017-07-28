## DIY 1

f = codecs.open('data/austen-emma-excerpt.txt', 'r', 'utf-8')
# insert your code here
# important: remember to properly close your file again!
lengths = []
for line in f:
    lengths.append(len(line))
f.close()
average = sum(lengths)/len(lengths)
print(average)

## DIY 2
f_in = codecs.open('data/austen-emma-excerpt-tokenised.txt', 'r', 'utf8')
text = f_in.read()
f_in.close()
words = text.lower().split()
words = list(set(words))
words = sorted(words)
print(words)

f_out = codecs.open('data/words.txt', 'w', 'utf-8')
for w in words:
    f_out.write(w + "\n")
f_out.close()

## DIY 3
filenames = os.listdir('data/arabian_nights')
print(len(filenames))

counter = 0
while counter < 1001:
    counter += 1
    filename = str(counter) + ".txt"
    if filename not in filenames:
        print(filename, "is missing!")

## DIY 4
os.mkdir('data/1001')
for fn in os.listdir('data/arabian_nights'):
    missing_zeroes = 8-len(fn) # e.g. 2.txt has a string length of 5, so it is missing 3 zeroes.
    new_fn = missing_zeroes * "0" + fn
    shutil.copyfile(os.path.join('data/arabian_nights', fn), os.path.join('data/1001', new_fn))

### Final exercises
## Ex. 1
from string import punctuation as punct

f_in = codecs.open("earnest.txt", "r", "utf-8")
text = f_in.read()
f_in.close()
text = text.lower() # Ignore capitalization
words = text.split()
freq_dict = {}
for word in words:
    for p in punct: # Iterate over all punctuation marks
        word = word.replace(p, "") # and remove them from the word
    if word not in freq_dict:
        freq_dict[word] = 1
    else:
        freq_dict[word] += 1

# One possible solution of getting dictionary items by value
freq_word_pairs = []
for word in freq_dict:
    freq_word_pairs.append([freq_dict[word], word]) # Add sublists of the form [frequency, word]
freq_word_pairs.sort() # Sorting will sort them on the frequency first

f_out = codecs.open("frequencies.txt", "w", "utf-8")
for freq, word in freq_word_pairs:
    f_out.write(word + "\t" + str(freq) + "\n")
f_out.close()

## Ex. 2
f_in = codecs.open("earnest.txt", "r", "utf-8")
text = f_in.read()
f_in.close()

text_starring_me = text.replace('Algernon', "Bart")

f_out = codecs.open("starring_me.txt", "w", "utf8")
f_out.write(text_starring_me)
f_out.close()

## Ex. 3
f_in = codecs.open("earnest.txt", "r", "utf-8")
f_out = codecs.open("earnest_numbered.txt", "w", "utf8")
counter = 0
for line in f_in:
    counter += 1
    f_out.write(str(counter) + " " + line)
f_in.close()
f_out.close()

## Ex. 4 was moved to Chapter 6, since it requires you to
## write your own functions. Apologies if you spent 3 sleepless
## nights trying to solve it. Also remember that all time spent
## programming is time well spent.