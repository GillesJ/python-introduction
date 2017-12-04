def add(l_numbers):
    return sum(l_numbers)


def multiply (l_numbers):
   import operator
   import functools
   return functools.reduce(operator.mul, l_numbers, 1)


l_numbers= [1,2,3,4]
print(add(l_numbers))
print(multiply(l_numbers))

