"""
###########################################################
Name: Robinson Umeike
Course: Analysis of Operating System
Course Code: CS 606
File: Homework #1
###########################################################
"""


from socket import *
from config import *

# Function to get user input
def get_input():
    input_str = input("\nPlease enter a number between 1 - 50 (Enter 'STOP' to end the program): ")
    return input_str

# Function to validate user input
def check_valid_input():
    while True:
        input_str = get_input()
        if input_str.isdigit():  # Check if the input is a valid number
            input_number = int(input_str)
            if 1 <= input_number <= 50:
                print("The number entered is:", input_number)
                return input_number  # Return the valid input
            else:
                print("The entered number is not in the range [1, 50]. Please try again.")
        elif input_str.lower() == "stop":  # Check if the user wants to stop the program
            print("Stopping program...")
            return None  # Return None to indicate stopping the program
        else:
            print("Input is not a valid number. Please try again.")

# Create a socket for the client
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Connect to the server (blocks until accepted)
i = 1

while True:
    # Call the function to get valid input
    valid_input = check_valid_input()

    if valid_input is None:  # Check if the user chose to stop the program
        break

    # Print a message indicating that the client has connected to the server
    print(f"Client{valid_input}_{i} has connected to the server.")
    
    # Convert the valid input to a string and send it to the server
    client_data = str(valid_input)
    client_socket.send(client_data.encode())  # Send the message
    
    # Print a message indicating the data sent to the server
    print(f"Client{valid_input}_{i} sent '{valid_input}' to the server.")
    
    # Receive and decode the response from the server
    processed_data = client_socket.recv(1024)
    processed_data = processed_data.decode()
    
    # Print the result received from the server
    print(f"Client{valid_input}_{i} received result: {processed_data}")
    
    i = i + 1

# Close the client socket connection
client_socket.close()
