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
    print (f"sending request")
    sock.sendall(file.encode())

    # Look for the response
    while True:
        data = sock.recv(1024)
        rec = open("received.jpg",'ab')
        if not data:
            rec.close()
            break
        rec.write(data)
    print ("File received")
    
finally:
    print ("closing")
    sock.close()
