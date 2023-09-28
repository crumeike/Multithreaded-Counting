import socket

def main():
    server_ip = '127.0.0.1'  # Change this to the server's IP address
    server_port = 50055      # Change this to the server's port number

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        number_input = input("Please enter a number (or 'STOP' to quit): ")
        if number_input == 'STOP':
            client.send(number_input.encode('utf-8'))
            break

        else:
            number = int(number_input)
            print(f"The number entered: {number}")
            client.send(str(number).encode('utf-8'))
            print(f"Client sent {number} to server")

            while(True):
                result = client.recv(1024).decode('utf-8')
                print(f"Client received result: {result}")
                if result == '8000':
                    break

    client.close()

if __name__ == '__main__':
    main()
