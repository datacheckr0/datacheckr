#! python3
# emailVerify.py - Verifies a single email based on deliverability and quality score

import requests

import json

API = "39481f9e97d7414ea3d674030f2e5483"

def get_email_data(email):
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={API}&email={email}"
    response = requests.get(url)

    # print(response.text)

    emailData = json.loads(response.text)

    return emailData

# Change function to create CSV later
def quality_score(emailData):
    q = emailData["quality_score"]
    e = emailData["email"]
    d = emailData["deliverability"].lower()
    print(f"The email {e} is {d} and the quality score is {q}")

email = input("Enter the email address that you want to verify: ")
emailData = get_email_data(email)

get_email_data(email)
quality_score(emailData)
