
import socket

TARGET_IP = "192.168.100.96"
TARGET_PORT = 5006

stringnih = "ABCDEFGHIJKLMNOPQRSTUV"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(stringnih.encode()),(TARGET_IP,TARGET_PORT))
