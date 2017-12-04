"""`arithmetic.py`: define a function add() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. 
For example, add([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""

def add(l):
	total = 0
	for x in l:
		total += x
	return(total)

def multiply(l):
	product = 1
	for x in l:
		product *= x
	return(product) 

l = [1, 2, 3, 4]

print(add(l))
print(multiply(l))