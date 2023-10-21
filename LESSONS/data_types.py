# String Data Type

# litereal assignment

import math
first = "Dolapo"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += '!'
print(fullname)

# Casting a number to a string
decade = str(1996)
print(type(decade))
print(decade)

statement = "I like football from the " + decade + "s."
print(statement)

# what if we want a statement with multiple lines
# Multiple lines

multilines = """

Hey, how are you?                                 

I was just checking in.  
                        All good?


"""
print(multilines)

# Escaping special characters

# Escaping special chaacters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'  # tab in sentence
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multilines.title())
print(multilines.replace("good", "ok"))
print(multilines)

print(len(multilines))
multilines += "                                                                           "
multilines = "                                                       " + multilines
print(len(multilines))

print(len(multilines.strip()))  # remove whitespace
print(len(multilines.lstrip()))  # remove left whitespace
print(len(multilines.rstrip()))  # remove right whitespace

print("")


# Build a menu

# You can call string methods directly on the value, it doesnt have to be on the variable name
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Buns".ljust(16, ".") + "31".rjust(4))
print("Doughnut".ljust(16, ".") + "$1.99".rjust(4))

print("")

# Sring index value
print(first[1])
print(first[-1])  # last value in the string
print(first[1:])  # provide range

# Some methods retuen boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean Data Type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

print("")
# Numeric Datatypes

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, bool))

# Float type

gpa = 3.28
y = float(1.123)
print(type(gpa))

print("")

# complex type
comp_value = 5+3j
print(comp_value.real)
print(comp_value.imag)

print("")

# Built in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print("")
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor
(gpa))
print(round(math.pi, 3))

print("")

#Cast a sting to a number