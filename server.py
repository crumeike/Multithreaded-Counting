from socket  import *
from constCS import * #-
from time import *


s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

(conn, addr) = s.accept()  # returns new socket and addr. client 
print(f"server has accepted: {conn}")
i = 0
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  msg = data.decode()+"*"  # process the incoming data into a response
  # print("Server sleeps before sending message...\n")
  # sleep(10)
  conn.send(msg.encode())  # return the response
  print(f"server sending message to {i}...")
  i += 1
conn.close()               # close the connection
print("server closed...")


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# s = socket(AF_INET, SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(5)  # Listen to up to 5 queued connections

# while True:
#   print("Waiting for a new connection...")
#   (conn, addr) = s.accept()  # Accept a new connection

#   while True:  # Loop to communicate with a single client
#       data = conn.recv(1024)  # Receive data from the client
#       if not data:
#           print("Client disconnected")
#           break  # Break the inner loop if the client disconnects
#       print("Server sleeps before sending message...\n")
#       sleep(5)
#       msg = data.decode() + "*"  # Process the incoming data into a response
#       conn.send(msg.encode())  # Return the response

#   conn.close()  # Close the connection with the client

