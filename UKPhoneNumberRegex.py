import re
UKNum = re.compile(r'(\+\d\d)?7\d\d\d\d\d\d\d\d\d$')

text = input()

UKNum.findall(text) == None:
    print('Number not found')
e



