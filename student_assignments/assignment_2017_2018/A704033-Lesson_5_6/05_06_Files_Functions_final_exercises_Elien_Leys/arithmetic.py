def add(nums):
	total = 0
	for n in nums:
		total+=n
	return total


def multiply(nums):
	total = 1
	for n in nums:
		total*=n
	return total

l = [1,2,3,4]
print(sum(l))
print(multiply(l))