#!/usr/bin/env/ python

def add(l):
	total = 0
	for number in l:
		total += number
	return total
	# You could also make this function a one-liner: return sum(l)

def multiply(l):
	total = 1
	for number in l:
		total *= number
	return total

numbers = [1, 2, 3, 4]
print(add(numbers))
print(multiply(numbers))