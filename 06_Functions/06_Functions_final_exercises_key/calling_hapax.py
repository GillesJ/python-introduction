#!/usr/bin/env/ python
import hapax3

print(hapax3.legomena("earnest.txt"))
print(hapax3.dislegomena("earnest.txt"))
print(hapax3.trislegomena("earnest.txt"))

# Or, alternatively:
from hapax3 import legomena, dislegomena, trislegomena

print(legomena("earnest.txt"))
print(dislegomena("earnest.txt"))
print(trislegomena("earnest.txt"))