def hello_world():
    print("Hello world")

hello_world()

# Sometimes, functions need to recieve data, and we can use placeholders for that data. These placeholders are called parameters


# def sum(num1, num2):
#     print(num1 + num2)

# sum(2,3)
# sum(2,3)
# sum(23,33) 

# Note: the argument is the actual data for when the function is called. Parameters are placeholders for the arguments.


# def sum(num1, num2=3):
#     if (type(num1) is not int or type(num2) is not int):
#         return 0
#     return num1 + num2

# total = sum(7, 2)
# print(total)


# def multiple_items(*args): #when you dont know how many arguments will be passed
#     print(args)
#     print(type(args))

# multiple_items("Dave", "John", "Sara")

# def mult_name_items(**kwargs):  #keyword arguments
#     print(kwargs)
#     print(type(kwargs))

# mult_name_items(first="Dave", last="John")


calc_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number =  int(user_input) # casting - turning a value from one data type to another

calc_value = days_to_units(user_input_number)
print(calc_value)
