from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib


fromaddr = "jgonz096@ucr.edu"
toaddr = "soliidsnakw93737@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

body = "Python test mail"
msg.attach(MIMEText(body,'plain'))


server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("solidsnake93737@gmail.com","lionheart73739---")
text = msg.as_string()
server.sendmail(fromaddr,toaddr.text)
