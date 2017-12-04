#calling_hapax.py: in this standalone script, import the functions from hapax3.py
# and call all three functions from there.
#Again, try them out on your Gutenberg-file.

from hapax3 import legomena,dislegomena,trislegomena

filename ="ThePictureOfDorianGray.txt"
result1 = legomena(filename)
print (result1)
result2= dislegomena(filename)
print (result2)
result3 = trislegomena(filename)
print (result3)

