# def get_valid_input():
#     while True:
#         input_str = input("Please enter a number between 1 - 50: ")
#         if input_str.isdigit():
#             input_num = int(input_str)
#             if 1 <= input_num <= 50:
#                 return input_num
#             else:
#                 print("The entered number is not in the range [1, 50]. Please try again.")
#         else:
#             print("Input is not a valid number. Please try again.")

# # Call the function to get valid input
# valid_input = get_valid_input()
# print("The number entered is:", valid_input)

from socket import *
from constCS import *
import threading

def count_up_to_n(number):
    # Implement the counting logic here
    # You can use a for loop to count up to 'number'
    pass

def handle_client(client_socket, address):
    print(f"Server accepted connection from {address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        try:
            number = int(data.decode())
            print(f"Server counts {number} in thread {threading.current_thread().ident} for {address}")
            result = count_up_to_n(number)
            client_socket.send(str(result).encode())
            print(f"Server sent result: {result} to {address}")
        except ValueError:
            print(f"Invalid input received from {address}")

    client_socket.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print("Server listening...")

while True:
    client_socket, client_address = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
