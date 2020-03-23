import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 1516)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)
message = ("upload upload.txt")
file_name = "".join(message.split()[1])
#print("namafile: ",file_name)

f = open(file_name, "rb")
length = len(file_name) + 1
file_content = base64.encodebytes(f.read())
f.close()

f = open("base64encode","wb")
f.write(file_content)
f.close

f = open("base64encode","rb")
pesan = message.encode() + (b" ") + f.read(1024)
#print("isi pesan: ",pesan)

while (pesan):
    sock.send(pesan)
    pesan = f.read(1024)
    data = sock.recv(1024)

#print("data: ",data)
print(message + " sukses!")
sock.close()