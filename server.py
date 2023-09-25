from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
print("server listening...")

(conn, addr) = s.accept()  # returns new socket and addr. client 
print(f"server has accepted: {conn}")
i = 0
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  msg = data.decode()+"*"  # process the incoming data into a response
  conn.send(msg.encode())  # return the response
  print(f"server sending message to {i}...")
  i += 1
conn.close()               # close the connection
print("server closed...")
