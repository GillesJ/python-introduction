testlist = [1,2,3,4]

def add(list):
	sum = 0
	for item in list:
		sum += item
	return sum

def multiply(list):
	product = 1
	for item in list:
		product *= item
	return product

print("sum:",add(testlist))
print("product:",multiply(testlist))
