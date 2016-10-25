### Conditions
weight = 45
if weight > 50:
    print("There is a $25 charge for luggage that heavy.")
elif weight < 50:
    print("Thank you for your business.")
else:
    print("Pfiew! The weight is just right!")

### and, or, not
if ("a" in word) or ("z" in word):
    print("a or z are in " + word)
else:
    print("None of the letters were found")

### DIY
numbers = []
if not numbers:
    print("This is an empty list")

numbers = []
if len(numbers) == 0:
    print("This is an empty list")

### Final exercises
## Ex. 1
score = 46
if score >= 80:
    grade = 'A'
elif score >= 65:
    grade = 'B'
elif score >= 50:
    grade = 'C'
else:
    grade = 'D'
print('Your score was ' + str(score) + ', so your grade is ' + grade + '.')

## Ex. 2
score = 98.0
if score >= 60.0: # Traversal of an if-elif-else decision tree ends on the first condition that is True.
    grade = 'D'
elif score >= 70.0: # As a result, these 'extra' constraints will never be checked because if they are True, the above statement must be as well.
    grade = 'C'
elif score >= 80.0:
    grade = 'B'
elif score >= 90.0:
    grade = 'A'
else:
    grade = 'F'
print(grade)

## Ex. 3
nr1 = 3
nr2 = 4

if nr1 > nr2:
    print(str(nr1))
elif nr1 == nr2:
    print("They're equal!")
else:
    print(str(nr2))