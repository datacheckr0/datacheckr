import ezsheets

def get_email_addresses(spreadsheet_url):
    # Load the Google Sheets spreadsheet
    spreadsheet = ezsheets.Spreadsheet(spreadsheet_url)

    # Get the first sheet (assumes responses are on the first sheet)
    sheet = spreadsheet[0]

    # Get all values from the 'Email Address' column (assuming it's column A)
    email_column = sheet.getColumn(3)

    # Skip the header row (assuming it's in row 1)
    email_addresses = email_column[1:]

    return email_addresses

def main():
    # Replace 'YOUR_SPREADSHEET_URL' with the URL of your Google Sheets spreadsheet
    spreadsheet_url = '1_4VtjeazqeWbpqf7QCny513VHGsbgYY18MRPVaD063k'

    # Get the email addresses from the spreadsheet
    email_addresses = get_email_addresses(spreadsheet_url)

    # Print the list of email addresses
    print("List of Email Addresses:")
    for email in email_addresses:
        print(email)

if __name__ == "__main__":
    main()

