import smtplib
from smtplib import SMTPException
sender = 'solidsnake93737@gmail.com'
receivers = 'solidsnake93737@yahoo.com'

subj='theSubject'
date = '2/1/2010'
message = "Hello from the trap"

username = str(sender)
password = str('lionheart73739---')


try:
	server = smtplib.SMTP("smtp.gmail.com",587)
	print username
	print password
	server.starttls()
	server.login(username,password)
	print 'x'
	server.sendmail(sender,receivers,message)
	server.quit()
	print "Successfully sent email"
except SMTPException:
	print "Error: unable to send email"
