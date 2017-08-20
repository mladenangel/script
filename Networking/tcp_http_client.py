# Simple HTTP TCP client

import socket

target_host='www.google.com'
target_port=80

# Create a socket object

client_http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client

client_http.connect((target_host, target_port))

# Send Data

client_http.send('GET / HTTP/1.1\r\nHost:google.com\r\n\r\n')

# Receive Data

response = client_http.recv(4096)
print(response)

# Mladen Angelov 2001
