import socket
import sys
import getpass

def run_client():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
	while ((reply.find('goodbye') < 0) and (reply.find('best') < 0)):
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
