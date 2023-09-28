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
from multiprocessing import Process
from threading import Thread
from time import sleep, time

# Function to perform a computation based on decoded data and send the result back to the client
def counting(decoded_data, Thread_id, client_socket):
    x = 0.0
    number = int(decoded_data)  # Convert the decoded data to an integer
    count = number * 8000000
    start = time()
    for i in range(count):
        x = x + 1.0
    end = time()
    results = end - start  # Calculate the time taken for computation correctly
    print(f"Server sent result >>> {results} to client_socket: {client_socket}")
    # Send the processed data back to the client
    processed_data = str(results)  # Convert the result to a string
    client_socket.send(processed_data.encode())

# Function to handle communication with a client
def handle_client(client_socket, client_id):
    Thread_id = 1
    while True:
        data = client_socket.recv(1024)
        if not data:
            break  # Stop if the client stopped sending data
        decoded_data = data.decode()  # Process the incoming data into a response
        print(f"Server counts '{decoded_data}' in thread_{Thread_id} for client_{client_id} >>> {client_socket}")
        thread = Thread(target=counting, args=(decoded_data, Thread_id, client_socket))
        thread.start()
        print(f"Thread{Thread_id} is going to sleep...")
        sleep(2)  # Sleep for 2 seconds
        Thread_id += 1

# Function to start the server
def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    print(f"Server is listening on {HOST}:{PORT}")

    client_id = 1

    while True:
        # Accept a client connection
        (client_socket, client_address) = server_socket.accept()
        print(f"Server accepted connection from client_{client_id}: \nclient_address>>> {client_address} \nclient_socket >>> {client_socket}")
        print(f"client_{client_id}")
        # Create a new process to handle the client
        client_process = Process(target=handle_client, args=(client_socket, client_id))
        client_process.start()
        print(f"Server is going to sleep...")
        sleep(2)  # Sleep for 2 seconds
        client_id += 1  # Increment client_id for the next client

if __name__ == '__main__':
    # Start the server in its own process
    server_process = Process(target=start_server)
    server_process.start()
    server_process.join()
