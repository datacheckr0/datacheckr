# Code identifies UK numbers within a string of text
def isPhoneNumber(text):
    if len(text) != 11:
        return False
    for i in range(0, 11):
        if not text[i].isdecimal():
            return False
    for i in range(0, 11):
        if not text[0:2] == '07':
            return False
    return True

message = input()
for i in range (len(message)):
    chunk = message[i:i+11]
    if isPhoneNumber(chunk):
        print('UK Phone number found: ' + chunk)
print('Done')
