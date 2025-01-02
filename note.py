# Different methods in the list:
# 1. append
# 2. insert
# 3. index
# 4. remove
# 4. remove
# 5. extend
# 6. pop 
# 7. copy or slicing is the same [:]
# 8. sort
# 9. count
# 10. reverse


# print ("This is the true essenf eof an eduai and ")




print("This is the simple play calculator.")
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        print("Division by zero is not allowed.")
        return None
    else:
        return x / y

def play_game():
    try:
        first_value = int(input("Enter your first value: "))
        second_value = int(input("Enter your second value: "))
        user_ask = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))
        
        if user_ask == 1:
            result = addition(first_value, second_value)
            print(f"The result of addition is {result}")
        elif user_ask == 2:
            result = subtraction(first_value, second_value)
            print(f"The result of subtraction is {result}")
        elif user_ask == 3:
            result = multiplication(first_value, second_value)
            print(f"The result of multiplication is {result}")
        elif user_ask == 4:
            result = division(first_value, second_value)
            if result is not None:
                print(f"The result of division is {result}")
        else:
            print("Your inputted value must be in the range of 1 to 4.")
            play_game()  # Restart the game if the input is invalid
    except ValueError:
        print("Please enter valid integer values.")
        play_game()  # Restart if non-integer input is given

def play_again():
    user_input = input("Do you want to calculate more? Enter 'Yes' or 'No': ")
    if user_input.lower() == "yes":
        play_game()
        play_again()  # Ask again after playing
    else:
        print("Thank you for playing this game.")

# Start the game
play_game()
play_again()
