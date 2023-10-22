

# Ternary Operator

# meaning = 42
# print('')

# print('Right on') if meaning > 10 else print('Not Today!')

# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

# new_points =alien_0['points']
# print(f"You have just earned {new_points} points!")


# class book:
#     def __init__(self) -> None:
#         self.color = "White"
#         self.author = "Gordon Lindsay"
#         self.title = "Answers to the difficult questions concerning healing"

# book = book()
# print(book.title)
# print(book.author)
# print(book.color)

# Dictionries are used to store data values that are in key value pairs

# band = {
#     "vocals": "Plant",
#     "guitar": "Page"
# } #method1 of creating dictionaries

# band2 = dict(vocals="Plant", guitar="Page" ) #method2

# print(band)
# print(band2)
# print(type(band2))
# print(len(band2))

# #How to access items

# print(band["vocals"])
# print(band.get("guitar"))

# #list all keys
# print(band.keys())

# #list all values
# print(band.values())

# #list of key/value pairs as tuples
# print(band.items())

# #veerify a key exist
# print("guitar" in band)
# print("triangle" in band)

# #change values
# band["vocals"] = "Coverdale"
# band.update({"bass": "JPG"})

# print(band)

# #remove items

# print(band.pop("bass"))
# print(band)

# band["drums"] = "Bonham"
# print(band)

# print(band.popitem()) #tuple
# print(band)

# #delete and clear
# band["drums"] = "Bonham"
# del band["drums"]
# print(band)

# band2.clear()
# print(band2)

# del band2

# # Copy Dictionaries

# band2 = band # create a reference
# print("Bad Copy!")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print(f"Original postion: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


#A dictionary of similar objects

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'eddie': 'ruby',
    'phil': 'python',
}

language = fav_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

#Using get to access values

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


Biodata = {
    'first_name': 'toluwanimi',
    'last_name': 'osuolale',
    'age': '22',
    'city': 'ibadan',
}


print(Biodata['first_name'].title())
print(Biodata['last_name'].title())
print(Biodata['age'].title())
print(Biodata['city'].title())

fav_numbers = {
    'tolu': '7',
    'dolapo': '10',
    'favour': '22',
    'jacob': '44',
}

num = fav_numbers['tolu']
print(f"Tolu's favorite number is {num}")

num = fav_numbers['dolapo']
print(f"Dolapo's favorite number is {num}")

num = fav_numbers['favour']
print(f"Favour's favorite number is {num}")
      
num = fav_numbers['jacob']     
print(f"Jacob's favorite number is {num}")

#Glossary

prog_words = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

word = 'string'
print(f"\n{word.title()}: {prog_words[word]}")

word = 'comment'
print(f"\n{word.title()}: {prog_words[word]}")

word = 'list'
print(f"\n{word.title()}: {prog_words[word]}")

word = 'loop'
print(f"\n{word.title()}: {prog_words[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {prog_words[word]}")

#looping through a dictionary

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

print("")

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("")


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


#looping through all the keys
print("")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
# for name in favorite_languages.keys():
#     print(name.title())

print("")

friends =['phil', 'sarah', 'jen']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t Hi, {name.title()}, I see you love {language}")