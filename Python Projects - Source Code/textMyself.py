#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string

# Preset values:
accountSID = 'AC91a178375cec997e559cfe02f908cd5a'
authToken = '805bf5551fa36064e17c49cf27027b74'
myNumber = '+447507613115'
twilioNumber = '+447700146989'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)


