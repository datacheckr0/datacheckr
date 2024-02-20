from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
import time

class PowerDialer:
    def __init__(self, twilio_account_sid, twilio_auth_token, twilio_phone_number):
        self.client = Client(twilio_account_sid, twilio_auth_token)
        self.twilio_phone_number = twilio_phone_number

    def dial_number(self, contact):
        call = self.client.calls.create(
            url=self.get_twiml_url(),
            to=contact.phone_number,
            from_=self.twilio_phone_number
        )

        # Simulate the call duration
        time.sleep(10)
        self.handle_call_status(call.status)

    def get_twiml_url(self):
        # This function generates TwiML (Twilio Markup Language) for the call
        response = VoiceResponse()
        response.gather(numDigits=1, action='/handle-key', method='POST')
        response.say('Hello! Press 1 to connect to the call.')
        return str(response)

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

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

def main():
    # Set your Twilio credentials and phone number
    twilio_account_sid = 'your_twilio_account_sid'
    twilio_auth_token = 'your_twilio_auth_token'
    twilio_phone_number = 'your_twilio_phone_number'

    # Sample contacts
    contacts = [
        Contact("John Doe", "+15558675309"),
        Contact("Jane Smith", "+15558675310"),
        # Add more contacts as needed
    ]

    power_dialer = PowerDialer(twilio_account_sid, twilio_auth_token, twilio_phone_number)

    for contact in contacts:
        power_dialer.dial_number(contact)

if __name__ == "__main__":
    main()

