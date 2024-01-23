# Ask for user name
user_name = input("What is your name?")

# Initialize flag variables
keep_going = 'y'
input_valid = False

# Loop to start the program and continue the program based on user response.
while keep_going != 'n':
    # Loop to get user input and check if it's valid
    while not input_valid:
        user_input = int(input("Please enter a number between 1 and 100: "))
        if user_input < 1 or user_input > 100:
            print("That is not a valid input!")
        else:
            input_valid = True
        print()

    # Use if/else statements to check conditions
    if user_input % 2 != 0 and user_input < 60:
        print(f"{user_name}, odd and less than 60.")
    elif user_input % 2 == 0 and user_input in range(2, 25):
        print(f"{user_name}, even and less than 25.")
    elif user_input % 2 == 0 and user_input in range(2, 61):
        print(f"{user_name}, even and between 26 and 60 inclusive.")
    elif user_input % 2 == 0 and user_input > 60:
        print(f"{user_name}, even and greater than 60.")
    elif user_input % 2 != 0 and user_input > 60:
        print(f"{user_name}, odd and greater than 60.")

    # Ask if user wants to continue and reset the valid input flag
    keep_going = input(f"Would you like to continue, {user_name}? (y/n)")
    input_valid = False
