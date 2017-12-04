#!/usr/bin/env/ python

def add(li):
	som = 0
	for n in li:
		som +=n
	return som
	

def multiply(li):
	product = 1
	for n in li:
		product *=n
	return product


li = [1, 2, 3, 4, 5, 6]

print(add(li), multiply(li))
