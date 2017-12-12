#export TWILIO_ACCOUNT_SID='AC70ae102e0d6f11f826857b5baea76c3f'
#export TWILIO_AUTH_TOKEN='99a18fe57d3de06ac661f52ae7f2bd41'
from twilio.rest import Client
client = Client('AC70ae102e0d6f11f826857b5baea76c3f','99a18fe57d3de06ac661f52ae7f2bd41')

client.messages.create(
from_='19093216714',
to='19097497707',
body='Greetings from TrapMaster69@420blzit.com! You\'ve caught something!',
media_url="/home/pi/Desktop/image.jpg")

