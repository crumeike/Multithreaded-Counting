def get_valid_input():
    while True:
        input_str = input("Please enter a number between 1 - 50: ")
        if input_str.isdigit():
            input_num = int(input_str)
            if 1 <= input_num <= 50:
                return input_num
            else:
                print("The entered number is not in the range [1, 50]. Please try again.")
        else:
            print("Input is not a valid number. Please try again.")

# Call the function to get valid input
valid_input = get_valid_input()
print("The number entered is:", valid_input)