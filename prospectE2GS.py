#! python3
# prospectE2GS.py - Finds relevant prospect data from a CSV export and automatically whitespaces Google Sheets
# Run code through Zapier/Make integrations

import ezsheets
import openpyxl

import sys

from textMyself import textmyself

def update_google_sheets(excel_file_path, google_sheets_key, start_row, end_row, columns):
    # Load Excel workbook
    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb.active

    # Authenticate with Google Sheets API using ezsheets
    ss = ezsheets.Spreadsheet(google_sheets_key)

    # Get the first sheet of the Google Spreadsheet
    google_sheet = ss[0]

    # Initializing row number
    row_num = start_row

    # Loop through the Excel sheet until end_row is encountered
    while row_num <= end_row:

        # Extract data from specified columns
        data = [sheet[col + str(row_num)].value for col in columns]

        # Update specific Cells in Google Sheets
        google_sheet.updateRow(row_num, data)

        row_num += 1

    return ss

def save_as_csv(ss):
    # Name the csv file
    csv_file_name = input("Name your CSV file")

    # Use the downloadAsCsv function to download the Google Sheets as CSV
    ss.downloadAsCSV(filename=csv_file_name)

    textmyself(f'CSV file saved as {csv_file_name}')


if __name__ == "__main__":
    # Prompt the user to enter the Excel file path
    excel_file_path = input("Add Excel file path: ")

    # Prompt the user to enter the Google Sheets key (URL)
    google_sheets_key = input("Add Google Sheets URL: ")

    # User input for start row, end row and columns to copy
    start_row = int(input("Input the row number you want to start from: "))  
    end_row = int(input("Input the row number you want to end at: ")) 
    cols = input("Input the column letters you want to copy, separated by commas (like 'A,B,C'): ").split(',')  # Columns to copy

    ss = update_google_sheets(excel_file_path, google_sheets_key, start_row, end_row, cols)

    # Save the Google Sheets as CSV
    csv_option = input("Do you want to save AS A CSV file? (Yes/No): ")
    if csv_option.lower() == "yes":
        # Save the Google Sheets as CSV
        save_as_csv(ss)