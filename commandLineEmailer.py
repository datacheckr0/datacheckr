#! python3
# commandLineEmailer.py - Sends email based on address and string given to command line
# Use Bright Data web browser to get around browser access

import requests, bs4, sys, os, pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def command_line_emailer():

    # Using selenium, log in to email address
    #url = 'ADD URL AFTER GETTING BROWSER'
    browser = webdriver.Chrome()
    res = browser.get(url)

    emailElem = browser.find_element(By.ID, "identifierId")
    emailElem.send_keys("demi.kotun1@gmail.com")
    emailElem.send_keys(Keys.ENTER)

    passElem = browser.find_element(By.ID, "password")
    passElem.send_keys("Manchester312")
    passElem.send_keys(Keys.ENTER)

    # Take email address and string of text on the command line
    if len if len(sys.argv) != 3:
        print('Please enter an address and string of text to send')

    recAddress = sys.argv[1]
    recMessage = sys.argv[2]

    # TODO: Send an email of the string to the provided address
    writeEmail = browser.find_element(By.CLASS_NAME, "T-I T-I-KE L3")
    writeEmail.click()

    pyperclip.copy(sys.argv[1])
    recEmail = browser.find_element(By.ID, ":vi")
    recEmail.send_keys(Keys.CONTROL, 'v')

    # TODO: Copy string for body, find HTML element, paste text, find and click send element to send email


#command_line_emailer()
#print('Email Sent')


