import socket
import threading
from colorama import *
bind_ip = '127.0.0.1'
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5)
print(Fore.RED+Back.WHITE+'[*] Listening on %s:%d' %(bind_ip,bind_port)+Style.RESET_ALL)
# this is our client-handling thread
def handle_client(client_socket):
    #print out what the cliend sends
    request = client_socket.recv(1024)
    print(Fore.BLUE+Back.WHITE+'[*] Received: %s' %request+Style.RESET_ALL)
    #send back a packet
    client_socket.send('[*] Delwin TCP server')
    client_socket.close()
while True:
    client, addr = server.accept()
    print(Fore.RED+Back.WHITE+'[*] Accepted connection from: %s:%d' %(addr[0],addr[1])+Style.RESET_ALL)
    # spin up our client thred to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()


