#! python3
# emailFinder.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# A Regex for emails
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                      # username
    @                                      # @ symbol
    [a-zA-Z0-9.-]+                         # domain name
    (\.[a-zA-Z]{2,4})                      # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in emailRegex.findall(text):                          # For email addresses, append group[0] of each match to the matches list
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No email addresses found.')

