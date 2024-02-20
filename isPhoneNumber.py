def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range (len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# For the first iteration of the loop (when i is 0), message[i:i+12] extracts a substring starting from the 0th character (the first character of the message) up to the character at index 11 (12 characters in total).
# For the second iteration (when i is 1), the slice starts from the 1st character and ends at the 12th character.
# This process continues for each iteration of the loop, extracting overlapping 12-character substrings from the message one at a time.
# The purpose of this slicing is to check each 12-character substring to see if it matches the format of a phone number (e.g., '415-555-1011').
