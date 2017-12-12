#Name: Jorge Gonzalez
#Username: jgonz096
#SID:861112270
#Class: CS179j

import socket
import sys
import getpass


#function for making a client connection
def run_client():
	#try to connect or else send an error
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error:
		print 'Failed to create socket'
		sys.exit()
	print 'Socket Created'

	#HOST = '192.168.1.18';
	HOST = '192.168.43.77';
	PORT = 2222;

	#Attempt to connect to host, or else error
	try:
		remote_ip = socket.gethostbyname(HOST)
	except socket.gaierror:
		print 'Hostname could not be resolved. Exiting'
		sys.exit()

	s.connect((remote_ip, PORT))

	print 'Socket Connected to ' + HOST + ' on ip ' + remote_ip

	input = ''
	reply = ''
	i = 0
	# while (s.recv(4096) == 0):
	#	print('')
	# reply = s.recv(4096)
	# print reply

	# s.sendall('')

	reply = s.recv(4096)
	print reply
	#print reply.find('goodbye')
	#print reply.find('best')
	while ((reply.find('goodbye') < 0) and (reply.find('fridge') < 0) and (reply.find('best') < 0)):
		input = raw_input()
		if not input:
			input = ' '
		s.send(input)
		reply = s.recv(4096)
		print reply
		#print reply.find('goodbye')
		#print reply.find('best')


	s.close()


#run_client()
