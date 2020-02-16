import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    file = "sent.jpg"
    open_file = open(file,'rb')
    read_file = open_file.read()
    print (f"sending {read_file}")
    sock.sendall(read_file)
    print("file sent.")
finally:
    print ("closing")
    sock.close()
