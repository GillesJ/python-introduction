"""dice.py: write a script that rolls a dice every time you run it, by generating and printing a random integer between 1 and 6! 
You can import functionality for doing this via random.randint()."""

from random import randint

def roll():
	print(randint(1,6))

print("Rolling the dice...")
roll()