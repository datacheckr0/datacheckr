#! python3
# countdown.py - A simple countdown script

import time, subprocess, webbrowser

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', 'alarm.wav'])

webbrowser.open('https://developer.royalmail.net')
