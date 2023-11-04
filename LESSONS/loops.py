# While loops  - executes a block of code while the condition is true

# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1  #increment every time it goes through the loop and it will eventually be equal to 10 or greater and the loop will stop


# value = 1
# while value <= 10:
#     value += 1 
#     if value == 5:
#         continue
   
#     print(value)
# else:
#     print("Value is now equal to  " + str(value))


#For loops - iterates over a sequence

names = {"Dave", "Sara", "Tolu"}
# for name in names:
#     print(name)

# for x in "Burkinafaso":
#     print(x)

# for name in names:
#     if name == "Sara":
#         break
#     print(name)

# for name in names:
#     if name == "Sara":
#         continue
#     print(name)

# Ranges

for x in range(4):
    print(x)

print("")

# for x in range(2, 9):
#     print(x)

for x in range(5, 101, 5):  #start at 0, go through 100, but increment by 5
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "Tolu"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + "." )


for action in actions:
    for name in names:
        print(name + " " + action + "." )