from socket  import *
from config import * 

def get_valid_input():
    while True:
        input_str = input("Please enter a number between 1 - 50: ")
        if input_str.isdigit():
            input_num = int(input_str)
            if 1 <= input_num <= 50:
                return input_num
            else:
                print("The entered number is not in the range [1, 50]. Please try again.")
        elif input_str.lower() == "stop":
            break
        else:
            print("Input is not a valid number. Please try again.")


# i = 0

# while True:

# Call the function to get valid input
valid_input = get_valid_input()
print("The number entered is: ", valid_input)

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
print("Client has connected to the server.")
msg = valid_input       # compose a message
s.send(msg.encode())    # send the message
print(f"Client sent {valid_input} to the server.")
data = s.recv(1024)     # receive the response
finaldata = data.decode()
print(f"Client received result: {finaldata}")    # print the result
s.close()               # close the connection

 # i= i + 1

