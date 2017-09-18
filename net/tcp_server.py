# TCP Server

import socket
import threading

# To start off, we pass the IP and port y start listenning
blind_ip = '0.0.0.0'
blind_port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((blind_ip, blind_port))

# Start listen
server.listen(5)

print ('[*] Listening on %s:%d' %(blind_ip, blind_port))

# This is client-handling thread !

def handle_client(client_socket):

# Print out whar the client sends
    request = client_socket.recv(1024)

# Send back a packet
    client_socket.send('DELWIN is THE BEST!')
    client_socket.send('Mest whit the best, die like rest')
    client_socket.close()

while True:
    client, addr = server.accept()
    print('[*] Accepted connection from:%s:%d' % (addr[0], addr[1]))

# Spin up our cliend thread to handle incoming data

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
#
# Mladen Angelov 2001
