#! python3
# bulkEmail.py - Loops through CSV of emails in bulk and verifies them

import requests

import json
import csv
import datetime
import time

API = "39481f9e97d7414ea3d674030f2e5483"

def csv_import():
    with open(csvInput, 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for original_row in csvReader:
            row = {k.lower(): v for k, v in original_row.items()}
            email = row.get("email")  # Use .get function to find ["email"]
            if email:  # Check if email is not empty or missing
                email_verification(email)
            else:
                print("No email found in this row. Make sure that you have a column with the 'email' label.")
            time.sleep(1)

def manual_input():
    emails = input("Enter the list of emails, separated by commas: ").split(',')
    for email in emails:
        email_verification(email.strip())  # We use .strip() to get rid of potential leading/trailing whitespaces
        time.sleep(1)

def get_email_data(email):
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={API}&email={email}"
    response = requests.get(url)

    # print(response.text)

    emailData = json.loads(response.text)

    return emailData

def email_verification(email):
    emailData = get_email_data(email)
    e = emailData.get("email")  # Defaults to None if 'email' key is not present
    d = emailData.get("deliverability") # Defaults to None if 'deliverability' key is not present
    q = emailData.get("quality_score")  # Defaults to None if 'quality_score' key is not present
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")

    # Write results to a csv file
    filename = f"results_{timestamp}.csv"
    with open(filename, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([e, d, q])

choice = input("Do you want to import a CSV file or input the emails manually? (Enter 'CSV' or 'manual'): ")

if choice.lower() == 'csv':
    csvInput = input("Add the name of your CSV file: ")
    print("Verifying All Emails...")
    csv_import()
elif choice.lower() == 'manual':
    print("Enter the emails you want to verify...")
    manual_input()

print("All emails have been checked")