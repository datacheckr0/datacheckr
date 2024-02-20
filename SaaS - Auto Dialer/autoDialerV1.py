# Auto dialer using Twilio - set up Twilio account and the necessary environment variables (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER).

import os
import time
from twilio.rest import Client

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AutoDialer:
    def __init__(self, contact_list):
        self.contact_list = contact_list
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
        self.client = Client(self.account_sid, self.auth_token)

    def dial_number(self, contact):
        print(f"Dialing {contact.name} at {contact.phone_number}")
        call = self.client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=contact.phone_number,
            from_=self.twilio_phone_number
        )
        # Simulate the call duration
        time.sleep(5)
        self.handle_call_status(call.status)

    def handle_call_status(self, status):
        if status == 'completed':
            print("Voice detected. Directing to call.")
        elif status == 'no-answer':
            print("No answer. Passing to the next contact.")
        elif status == 'busy':
            print("Line is busy. Passing to the next contact.")
        elif status == 'failed':
            print("Call failed. Passing to the next contact.")
        elif status == 'voicemail':
            print("Voicemail detected. Sending pre-recorded message.")

def main():
    # Sample contacts
    contacts = [
        Contact("John Doe", "+15558675310"),
        Contact("Jane Smith", "+15558675311"),
        # Add more contacts as needed
    ]

    auto_dialer = AutoDialer(contacts)

    for contact in contacts:
        auto_dialer.dial_number(contact)

if __name__ == "__main__":
    main()

# You'll need to replace the sample Twilio phone numbers and TwiML URL with your actual values
# Make sure to install the Twilio Python library by running: pip install twilio


