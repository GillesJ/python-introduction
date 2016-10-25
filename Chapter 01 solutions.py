### Minutes in seven weeks
print(60*24*7*7)

### blablah
original_string = "bla"
new_string = 2*original_string
print(new_string)
new_string = new_string+"h"
print(new_string)

### blablah shortcut
original_string = "blabla"
# manipulate original_string to add an 'h'...
original_string += "h"
print(original_string)

### Name
name = "Desmet"
print(name)

### Middle letters
middle_letters = name[2:-2]
print(middle_letters)

### Humanities
word1 = "human"
word2 = "opportunities"
print(word1 + word2[-5:])

### FINAL EXERCISES
### Ex. 1
cover_price = 24.95
store_price = cover_price / 100 * 60
price_first_book = store_price + 3
price_rest_books = (store_price + 0.75) * 59
wholesale = price_first_book + price_rest_books
print("The wholesale price is: " + str(wholesale))

### Ex. 2
print("A message"). # the dot at the end doesn't serve a function
print("A message')  # the quotation marks that enclose the string don't match (single vs. double)
print('A message"') # nothing is actually wrong with this: you can use double quotes inside single quotes and vice versa.

### Ex. 3
# ZeroDivisionError
0/5
5/0
# Note that 0/5 doesn't raise an error, but 5/0 does!

### Ex. 4
number = 9.5 * (4.5 - 2.5) * (345.5 - 3.5)
print(number)
str_number = str(number)
print(len(str_number))

### Ex. 5
a = 2
b = 20007
c = 5

print(str(a) + str(b)[1:3] + str(c))
print(((str(a) + str(c)) * 4) + str(a))
print(str(a) + str(c) + str(a * c))
print(b - b * 4 - 2 * a)
print(str(b)[:3] + str(a) + str(c) + (str(b)[-2:]))

### Ex. 6
var1 = 3
var2 = 6 # here, we define var2
var3 = 7
"""
Now we are going to calculate
the actual
average:
"""
average = (var1 + var2 + var3) / 3
print("The average is: " + str(average))

### Ex. 7
radius = 6
pi = 3.14159
surface = radius * radius * pi
print("The surface area of a circle with radius " + str(radius) + " is: " + str(surface) + ".")

### Ex. 7 interactive
radius = input("What is the radius? ")
radius = int(radius) # The interactive input is a string, so we need to cast it as an integer
pi = 3.14159
surface = radius * radius * pi
print("The surface area of a circle with radius " + str(radius) + " is: " + str(surface) + ".")

### Ex. 8
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

amount = 11.56
cents = 100 * amount

# dollars:
cents_for_quarters_and_smaller = cents % 100
dollars = (cents-cents_for_quarters_and_smaller) / 100

# quarters:
cents_for_dimes_and_smaller = cents_for_quarters_and_smaller % 25
quarters = (cents_for_quarters_and_smaller-cents_for_dimes_and_smaller) / 25

# dimes: 
cents_for_nickels_and_smaller = cents_for_dimes_and_smaller % 10
dimes = (cents_for_dimes_and_smaller-cents_for_nickels_and_smaller) / 10

# nickels (and pennies):
pennies = cents_for_dimes_and_smaller % 5
nickels = (cents_for_dimes_and_smaller-pennies) / 5

print("Dollars: " + str(int(dollars)))
print("Quarters: " + str(int(quarters)))
print("Dimes: " + str(int(dimes)))
print("Nickels: " + str(int(nickels)))
print("Pennies: " + str(int(pennies)))