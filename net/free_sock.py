# delwin

import socket
import sys

def reuse_sock_addr():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_state=sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print('Old state:%s,New state:%s'%(old_state,new_state))
    port = 8383

    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    srv.bind(('',port))
    srv.listen(1)
    print('Listening on port:%s' %port)
    while True:
        try:
            connection, addr=srv.accept()
            print('Connected by %s:%s' %(addr[0],addr[1]))
        except KeyboardInterrupt:
            break
        except (socket.error, msg):
            print('%s' %(msg,))

if __name__=='__main__':
    reuse_sock_addr()
 
