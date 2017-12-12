import socket
import sys
from thread import *
import getpass
from socket import timeout

#create hosr and port to bind to
HOST = ''
PORT = 2222

#create a socket for server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket Created'

#Attemp to bind socket s to host/port. If failed, print error and exit
try:
	s.bind((HOST,PORT))
except socket.error,msg:
	print 'Bind failed. Error Code: ' + str(msg[0]) + msg[1]
	sys.exit()
print 'Soocket bind complete'

#have socket listen and wait for a connection
s.listen(10)
print 'Socket now listening'


def clientthread(conn):
	conn.send('Please enter the pest for which you want bait or enter \"Quit\" to quit: \n')
	#data = conn.recv(4096)
	while 1:
		data = conn.recv(4096)
		if (data == 'mouse') or (data == 'Mouse') :
			msg = 'Cheese' + ' would be best!\n'
			conn.send(msg)
			break
		elif (data == 'quit') or (data == 'Quit') :
			msg = 'Okay, goodbye!\n'
			conn.send(msg)
			break
		else:
			msg = 'Invalid Input! Try another or quit: \n'
			conn.send(msg)

while 1:
	conn,addr = s.accept()
	print 'Conected with ' + addr[0] + ':' + str(addr[1])
	start_new_thread(clientthread,(conn,))
s.close()
