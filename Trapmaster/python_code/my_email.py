import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Hello from trap. You\'ve caught something!\n')

msg['Subject'] = 'Trap'
msg['From'] = 'Trapmaster69'
msg['To'] = 'solidsnake93737@gmail.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
