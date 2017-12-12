import socket
import sys
from thread import *
import getpass
from socket import timeout

HOST = ''
PORT = 2222

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket Created'

try:
	s.bind((HOST,PORT))
except socket.error,msg:
	print 'Bind failed. Error Code: ' + str(msg[0]) + msg[1]
	sys.exit()
print 'Soocket bind complete'

s.listen(10)
print 'Socket now listening'

clientList = []
comboList = []
#list[username,password,unread,read,friend requests,friends,timeline,newsfeed]]
clientList.append(['jcdenton','bionicman',[],[],[],[],[],[]])
clientList.append(['ajensen','mandrake',[],[],[],[],[],[]])
clientList.append(['ghermann','laputanmachine',[],[],[],[],[],[]])
clientList.append(['anavarre','flatlanderwoman',[],[],[],[],[],[]])
clientList.append(['jmanderley','knightkiller',[],[],[],[],[],[]])


username = ''
password = ''
#s.setblocking(0)

def clientthread(conn):
	#conn.setblocking(0)
	conn.send('Welcome to Facebook. Please enter your username and password.\n')
	#conn.send('Wow. much surprise!\n')
	#data = conn.recv(4096)
	i = 0
	userNumber = 0
	unreadMsgSize = 0
	readMsgSize = 0
	friendRequestSize = 0
	friendListSize = 0
	statusNumber = 1

	while 1:
		if(i == 0):
			conn.send('username: ')
			data = conn.recv(4096)
			if not data:
				break
			username = data
			print('username: ' + username)
			i = i + 1
			#username for username in clientList if username[0] == data
			
		elif(i == 1):
			#print('password: ')
			conn.sendall('password: ')
			data = conn.recv(4096)
			if not data:
				break
			password = data
			#conn.sendall(username)
			#conn.sendall(password)
			print('password: ' + password)
			#conn.send(loginstatus)

			login = [username,password]
			loginSuccessful = 0
			for combo in clientList:
				if(combo[0] == login[0] and combo[1] == login[1]):
					loginSuccessful = 1
					print('Login Successful!')
					#conn.send('Login Successful!')
					i = i + 1
					break
				userNumber = userNumber + 1
			if (loginSuccessful == 0):
				i = 0
				userNumber = 0
				conn.send('Invalid username/password combination. Try Again.\n')
			else:
				i = i + 1
		else:
			#unreadMsgSize = 0
			#readMsgSize = 0
			#friendRequestSize = 0
			#friendListSize = 0
			#statusNumber = 0
			
			#print(userNumber)
			#print('userNumber: ' + str(userNumber))
			if not clientList[userNumber][2]:
				unreadMsgSize = 0
			else:
				unreadMsgSize = len(clientList[userNumber][2])
			if not clientList[userNumber][3]:
				readMsgSize = 0
			else:
				readMsgSize = len(clientList[userNumber][3])
			if not clientList[userNumber][4]:
				friendRequestSize = 0
			else:
				friendRequestSize = len(clientList[userNumber][4])
			if not clientList[userNumber][5]:
				friendListSize = 0
			else:
				friendListSize = len(clientList[userNumber][5])


			menu = '\nWhat would you like to do:\n1. Change Password?\n2. Logout?\n3. See Unread Messages (' + str(unreadMsgSize) + ')\n4. See read Messages (' + str(readMsgSize) + ')\n5. Send Message\n6. Update\n7. Friend Requests (' + str(friendRequestSize) + ')\n8. Friends List (' + str(friendListSize) + ')\n9. Send Friend Request\n10. Timeline\n11. News Feed\n12. Make a post\n'
			conn.send(menu)
			data = conn.recv(4096)
			if not data:
				break
			if(data == '1'):
				conn.send('Please enter current password: ')
				data = conn.recv(4096)
				oldPassword = data
				if (oldPassword == password):	
					conn.send('Please enter new password: ')
					data = conn.recv(4096)
					newPassword = data
					password = newPassword
					clientList[userNumber][1] = password 
					print(clientList[userNumber])
				else:
					conn.send('Wrong Password!\n')
			elif(data == '2'):
				msg = 'Goodbye ' + username
				conn.send(msg)
				#print(msg[0:7])
				conn.close()
			elif(data == '3'):
				for item in clientList[userNumber][2]:
					print(item)
					conn.send(item[0])
					conn.send(' --- From ' + item[1] + '\n')
				clientList[userNumber][3] = clientList[userNumber][3] + clientList[userNumber][2]
				clientList[userNumber][2][:] = []		
			#	conn.send('\nPress Enter to continue.\n')
			#	print 'lol'
			#	data = conn.recv(4096)
			#	print 'lmfao'
			elif(data == '4'):
				for item in clientList[userNumber][3]:
					print(item)
					conn.send(item[0])
					conn.send(' --- From ' + item[1] + '\n')
			elif(data == '5'):
				conn.send('Please Enter a message: \n')
				data = conn.recv(4096)
				msgToSend = data
				conn.send('Who would you like to send a message too?')
				data = conn.recv(4096)
				receiver = data
				sender = username
				packet = [msgToSend,sender]
				print(packet)
				for item in clientList:
					if(item[0] == receiver):
						item[2].append(packet)
						print (item[2])
						break
			elif(data == '6'):
				conn.send('Update done!')
			elif(data == '7'):
				if not (clientList[userNumber][4]):
					conn.send('No pending friend requests at this time\n')
				else:
					for item in clientList[userNumber][4]:
						if item in clientList[userNumber][5]:
							conn.send(item + ' is already a friend.\n')
						else:
							question = 'Do you wish to accept(y) or reject(n) ' + item + '\'s friend request?\n'
							conn.send(question)
							answer = conn.recv(4096) 
							if(answer == 'y'):
								clientList[userNumber][5].append(item)
								for m in clientList:
									if(m[0] == item):
										m[5].append(username)
										break
					clientList[userNumber][4][:] = []
			elif(data == '8'):
				if not (clientList[userNumber][5]):
					conn.send('No Friends. Forever Alone :{c\n')
				else:
					conn.send('Friends:\n')
					for item in clientList[userNumber][5]:
						friend = item + '\n'
						conn.send(friend)
			elif(data == '9'):
				conn.send('Who would you like to send a friend request to?\n')
				data = conn.recv(4096)
				if(data == username):
					conn.send('Cannot friend yourself lol. Forever alone.\n')
				elif data in clientList[userNumber][5]:
					conn.send('You already have this person as a friend') 
				else:
					k = 0
					for item in clientList:
						if(item[0] == data):
							if (username in item[4]):
								conn.send('Friend request already pending\n')
								k = 1
								break
							else:
								item[4].append(username)
								k = 1
								break;
					if(k == 0):
						conn.send('User does not exist.\n')
				
			elif(data == '10'):
				conn.send('Timeline: \n')
				if not (clientList[userNumber][6]):
					conn.send('No statuses posted.\n')
				else:
					for item in clientList[userNumber][6]:
						conn.send(item[0] + ' --- ' + str(item[1]) + '\n')
			elif(data == '11'):
				count = 0
				#clientList[userNumber][7] = clientList[userNumber][7].sort(key=lambda number: number[1])
				#clientList[userNumber][7] = list(reversed(clientList[userNumber][7]))
				if not (clientList[userNumber][7]) or not (clientList[userNumber][5]):
					conn.send('Nothing to show.\n')
				else:
					conn.send('News Feed:\n')
					for item in clientList[userNumber][7]:
						if item[2] in clientList[userNumber][5]:
							conn.send(item[0] + ' --- ' + item[2] + ' - Post #' + str(item[1]) + '\n' )
							count = count + 1
						if (count == 10):
							break
								

			elif(data == '12'):
				conn.send('Enter a status: \n')
				status = conn.recv(4096)
				statusCombo = [status,statusNumber]
				if not clientList[userNumber][6]:
					clientList[userNumber][6].append(statusCombo)
				else:
					clientList[userNumber][6].insert(0,statusCombo)
				statusNumber = statusNumber + 1
				
				statusList = [statusCombo[0],statusCombo[1],username]
				for item in clientList:
					if not (item[7]):
						item[7].append(statusList)
					else:
						item[7].insert(0,statusList)
			else:
				if not data:
					break
			i = i + 1
		#print('lol')
		#else:
		#data = conn.recv(1024)
		#reply = 'OK...' + data
		#if not data:
		#	break
		#conn.send(reply)
	#conn.close()
while 1:
	conn,addr = s.accept()
	print 'Conected with ' + addr[0] + ':' + str(addr[1])
	start_new_thread(clientthread,(conn,))
s.close()
