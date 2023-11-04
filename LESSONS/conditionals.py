calc_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    # print(num_of_days  > 0)
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered zero, not valid. PLease eneter a valid positive number"

    # else:
    #     return "you entered a neagtive value, so no conversion for you"


def validate_and_execute():
    if user_input.isdigit():
    # user_input_number =  int(user_input) # casting - turning a value from one data type to another
        calc_value = days_to_units(int(user_input))
        print(calc_value)
    else:
        print("Your input is not a valid number")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

validate_and_execute()