import socket
import sys
import getpass

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()
print 'Socket Created'

HOST = '';
PORT = 2222;

try:
	remote_ip = socket.gethostbyname(HOST)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

s.connect((remote_ip,PORT))

print 'Socket Connected to ' + HOST + ' on ip ' + remote_ip

#message = "GET / HTTP/1.1\r\n\r\n"

#try:
#	s.sendall(message)
#except socket.error:
#	print 'Send failed'
#	sys.exit()
#print 'Message send successfully'

input = ''
i = 0
#while (s.recv(4096) == 0):
#	print('') 
#reply = s.recv(4096)
#print reply

#s.sendall('')
while (input != 'quit' and input != 'Quit'):
#	reply = s.recv(4096)
#	print reply
	#reply = s.recv(4096)
	#print(reply)
	#if(reply == 'password: '):
	#input = getpass.getpass('')
	#else:
		#input = raw_input()
	
	reply = s.recv(4096)
	print reply
	if (i == 0):
		i = i + 1
		input = ''
	#if(input == '3'):
	#	input = raw_input()
	#	reply = s.recv(4096)
	#	print reply
	else:
		if (reply == 'username: '):
			input = raw_input()
		elif (reply == 'password: ' or reply == 'Please enter current password: ' or reply == 'Please enter new password: ' ):
			input = getpass.getpass('')
		elif (reply[0:7] ==  'Goodbye'):
			s.close()
		else:
			input = raw_input()
	s.send(input)
	#i = i + 1

s.close()
