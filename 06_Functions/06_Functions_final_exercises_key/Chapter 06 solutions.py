## DIY 1
def count_articles(text):
    tokens = text.split()
    count = 0
    for token in tokens:
        if token.lower() in ('the', 'a', 'an'):
            count += 1
    return count
   
text = "A bit less trivial , this function counts the number of articles ( the , a , an ) in a list of words"
print(count_articles(text))

## DIY 2
# write your function calculate_average here
def calculate_average(numbers):
    average = sum(numbers)/len(numbers)
    return average

# do not modify the code below, for testing only
numbers = [1, 2, 3, 4, 5]
av = calculate_average(numbers)
print(av == 3) # should be True if you did it correctly

## DIY 3
# write your function textstats here
def textstats(filename):
    f = codecs.open(filename, "r", "utf-8")
    text = f.read()
    f.close()
    lines = len(text.split("\n"))
    tokens = len(text.split())
    chars = len(text)
    return lines, tokens, chars

# test
lines, tokens, chars = textstats("data/austen-emma-excerpt.txt")
print("Found", str(lines), "lines,", str(tokens), "tokens and", str(chars), "characters.")
