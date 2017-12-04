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
