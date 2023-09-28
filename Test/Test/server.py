import socket
import threading
import random
import time

# Function to simulate counting up to a number with optional sleep
def count_up_to(number, client_id, client_socket):

    for i in range(number, 8000+1):

        print(f"Server counts {i} in thread {client_id} for client {client_socket}")
        print(f"Server sent result: {i} to client {client_socket}")
        client_socket.send(str(i).encode('utf-8'))
        time.sleep(random.uniform(0.000, 0.005))



# Function to handle client requests
def handle_client(client_socket):
    client_id = threading.currentThread().getName()
    print(f"Server accepted connection from client {client_id}")
    
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if data == 'STOP':
                break
            try:
                number = int(data)
                print(f"Server counts {number} in thread {client_id} for client {client_socket}")
                count_up_to(number,client_id, client_socket)
             
            except ValueError:
                print("Invalid input. Please enter a valid number or 'STOP' to quit.")
        except ConnectionResetError:
            break
    
    print(f"Client {client_socket} disconnected")
    client_socket.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 50055

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)

    print("Server listening...")

    while True:
        try:
            client_socket, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            print("Server shutting down...")
            break

if __name__ == '__main__':
    main()
