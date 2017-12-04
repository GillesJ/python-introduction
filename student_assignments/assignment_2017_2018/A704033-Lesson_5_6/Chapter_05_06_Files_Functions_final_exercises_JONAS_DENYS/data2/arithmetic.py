def add(li):
	som = 0
	for number in li:
		som += number
	return som

def multiply(li):
	outcome = 1
	for number in li:
		outcome *= number
	return outcome

li = [1,2,3,4,5,6,7]
print(sum(li))
print(add(li))
print(multiply(li))