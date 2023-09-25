from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
i = 0 
while i < 2: 
    msg = "Hello World"     # compose a message
    s.send(msg.encode())    # send the message
    print(f"client_{i} sending message...")
    data = s.recv(1024)     # receive the response
    print(data.decode())    # print the result
    i += 1

s.close()               # close the connection
print("client closed...")