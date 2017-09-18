# Simpl UDP client

import socket

target_host='127.0.0.1'
target_port=7777

# Create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send Data

client.sendto('AAABBBCCC',(target_host, target_port))

# Reseave Data

data, addr = client.recvfrom(4096)
print data

# Mladen Angelov 2001

