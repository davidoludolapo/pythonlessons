calc_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):

    return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"


def validate_and_execute():
 

    try:
        user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
        user_input_number = int(user_input)
        if user_input_number > 0:
            calc_value = days_to_units(int(user_input))
            print(calc_value)
        elif user_input_number == 0:
            print("you entered zero, not valid. PLease eneter a valid positive number")
        else:
            print("You've entered a negative number")

    except ValueError:
        print("Your input is not a valid number")

while True:
    validate_and_execute()
