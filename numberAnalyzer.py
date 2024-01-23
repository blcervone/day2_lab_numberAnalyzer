user_name = input("What is your name?")
keep_going = 'y'
input_valid = False
while keep_going != 'n':
    while not input_valid:
        user_input = int(input("Please enter a number between 1 and 100: "))
        if user_input < 1 or user_input > 100:
            print("That is not a valid input!")
        else:
            input_valid = True
        print()
    if user_input % 2 != 0 and user_input < 60:
        print("Odd and less than 60.")
    elif user_input % 2 == 0 and user_input in range(2, 25):
        print("Even and less than 25.")
    elif user_input % 2 == 0 and user_input in range(2, 61):
        print("Even and between 26 and 60 inclusive.")
    elif user_input % 2 == 0 and user_input > 60:
        print("Even and greater than 60.")
    elif user_input % 2 != 0 and user_input > 60:
        print("Odd and greater than 60.")
    keep_going = input(f"Would you like to continue, {user_name}? (y/n)")
    input_valid = False
