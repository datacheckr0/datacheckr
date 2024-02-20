#! python3
# emailLoop.py - Takes an email address template and creates email addresses for all people within a company 

import ezsheets

import sys

def create_email(format, first_name, last_name, domain):
    format = format.replace('{first}', first_name.lower())
    format = format.replace('{last}', last_name.lower())
    format = format.replace('{initials}', first_name.lower()[0] + last_name.lower()[0])
    email = format + '@' + domain
    return email

def letter_to_number(letter):
    return ord(letter.upper()) - 64

spreadsheet_id = input("Input the Google Sheets ID: ")  # Google Sheets file ID
domain = input("Input the email domain (like 'company.com'): ")  # Domain for email
email_format = input("Input an example of the email format using the {first}, {last} or {initials} parameters: ")  # Email format
start_row = int(input("Input the row number you want to start from: "))  # Start row number (1-based)
end_row = int(input("Input the row number you want to end at: "))  # End row number (1-based)
first_name_column = letter_to_number(input("Input the column letter where First Names are: "))  # First Names column
last_name_column = letter_to_number(input("Input the column letter where Last Names are: "))  # Last Names column
email_column = letter_to_number(input("Input the column letter for email: "))  # Email column

ss = ezsheets.Spreadsheet(spreadsheet_id)
sheet = ss[0]  # Get the first sheet

print(f"Now looping through all contacts for {domain}")

for i in range(start_row, end_row + 1):  # Loop through, including the end row
    row = sheet.getRow(i)
    firstName = row[first_name_column - 1]  # -1 because Python indexing starts at 0
    lastName = row[last_name_column - 1]   # -1 because Python indexing starts at 0
    email = create_email(email_format, firstName, lastName, domain)
    row[email_column - 1] = email   # -1 because python indexing start at 0
    sheet.updateRow(i, row)  # Update with new email


# Save as CSV option
save_as_csv = input("Do you want to create a CSV file for the updated prospects? (Yes/No) ")
if save_as_csv.lower() == 'yes':
    # Create a new Spreadsheet and get its first sheet
    new_ss = ezsheets.createSpreadsheet(domain)
    new_sheet = new_ss[0]

    # Get user input for the rows and columns to be copied
    copy_start_row = int(input("Input the row number you want to start copying from: "))  # Start row number (1-based)
    copy_end_row = int(input("Input the row number you want to end copying at: "))  # End row number (1-based)
    copy_columns = input("Input the column letters you want to copy, separated by commas (like 'A,B,C'): ")  # Columns to copy
    copy_columns = [letter_to_number(col) for col in copy_columns.split(',')]

    new_sheet.clear()
    
    # Copy rows from the old sheet to the new sheet
    for row_num in range(copy_start_row, copy_end_row + 1):
        old_row = sheet.getRow(row_num)
        new_row = [old_row[col - 1] for col in copy_columns]
        new_sheet.updateRow(row_num, new_row)

    new_ss.downloadAsCSV()  # save as CSV
    print(f"The {domain} CSV file has been created")
else: 
    print("Program ended without creating a CSV file.")

print(f"All emails for {domain} have been created")