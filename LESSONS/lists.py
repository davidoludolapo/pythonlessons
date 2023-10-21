users = ['David', 'Sarah', 'John']

data = ['Dave', 32, True]

emptylist = []

print("Dave" in emptylist)

#get specific item from the list

print(users[0])
print(users[-1]) #print the last value in the list

#use methods to know the position of a value
print(users.index('Sarah'))

#get range of value
print(users[0:2])
print(users[1:])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Dolapo'])
print(users)

# users.extend(data) #pass in preexisting lists
# print(users)

#add item at the beginning

users.insert(0, 'Bob')
print(users)

users[2:2] =['Eddie','Alphie']
print(users)

#replace values
users[1:3] = ['Dammy', 'Toluwanimi']
print(users)

#remove data
users.remove('Bob')
print(users)

#remove last item from list
print(users.pop())
print(users)

#delte specific users

del users[0]
print(users)

#delete list completely

# del data
data.clear()
print(data)

users[1:2] =['dave']
users.sort()
print(users)
users.sort(key=str.lower)
print(users)

#numbers
nums =[4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

#what if we wanna kep the original list the way it was but yet sort the list just for individual purpose. Use the global approach

print(sorted(nums, reverse=True))
print(nums)

#make a copy of original ist and sort the copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

#Check the type of list
print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)


#Tuples - Very much like lists, but data in a tuple will not change 

mytuple = tuple(('Dave', 43, True))
anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Meal')
newtuple = tuple(newlist)
print(newtuple)

#unpack a tuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))