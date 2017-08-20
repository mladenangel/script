# Python netcat 
# Mladen Angelov 2011
import sys
import sockets
import getopt
import threading
import subprocess

# define some global varibles
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print('Python netcat')
    print()
    print('Usage: python_nc.py -t target_host -p port')
    print('-l --listen - listen on [host]:[port] for incoming connections')
    print('-e --execute=filo_to_run - execute the given file upon receiving a connection')
    print('-c --command - initialize a command shell')
    print('-u --upload=destination')
    print()
    print()
    print('Examples:')
    print('./python_nc.py -t 192.168.0.1 -p 5555 -l -c ')
    print('python python_nc.py -t 192.168.1.1 -p 5555 -l -u=c:\target.exe')
    print('python python_nc.py -t 192.168.1.1 -p 5554 -l -e=e\'cat /etc/passwd\'')
    print("echo 'ABCDEFGHI'| ./python_nc.py -t 192.168.1.1 -p 1234")
    sys.exit(0)

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
    	client.connect((target, port))
    	if len(buffer):
    		client.send(buffer)
    	while True:
    		recv_len = 1
    		response = ""
    		while recv_len:
    			    data = client.recv(4096)
    			    recv_len = len(data)
    			    response += data
    			    if recv_len < 4096:
    			    	break
    		print(response)
    		buffer = raw_input("")
    		buffer += "\n"
    		client.send(buffer)
    except:
    	print("[*] Exception! Exiting.")
    	client.close()
def server_loop():
    global target

    if not len(target):
        target = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)
    while True:
        client_thread = threading.Thread(target = (client_handler), args =(client_socket))
        client_thread.start()

def run_command():
    command = command.rstrip()
    try:
    	output = subprocess.check_output(command, stderr = subprocess.STDOUT, shell = True)

    except:
    	output = "Failed to execute command \r\n"

return output

def client_handler(client_socket):
	global upload
	global execute
	global command
    
	if len(upload_destination):
		file_buffer = ""
		while True:
			data = client_socket.recv(1024)
			if not data:
				break
			else:
			    file_buffer += data
		try:	    
			file_descriptor = open(upload_destination, "wb")
			file_descriptor.close()
		except:	
			client_socket.send("Failed to save")
    if len(execute):
    	output = run_command(execute)
    	client_socket.send(output)
    if command:
    	while True:
    		client_socket.send("<pyNC:#>")
                (enter key)    
    		cmd_buffer = ""
    		while "\n" not in cmd_buffer:
    			cmd_buffer += client_socket.recv(1024)
    		response = run_command(cmd_buffer)
    		client_socket.send(response)
    			


def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:])
	    usage()

	# read the commandline options
	try:    

		    opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help","listen", "execute","target","port","upload"])
    exept getopt.GetopError as err:
            print str(err)
            usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"
 
    # are we going to listen or just send data from stdin?
    if not listen and len(target) and port > a:
    	#
    	buffer = sys.stdin.read()
    	client_sender(buffer)
    if listen:
        server_loop()

main()

