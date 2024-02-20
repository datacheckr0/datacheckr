#! python3
# nordicFundingScraper.py - Scrapes funding news from Nordic data source Arctic Startup, and updates new posts to a database
# ChatGPT Source Template - Update code with relevant HTML and titles

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import ezsheets

# Function to scrape funding news from Arctic Startup
def scrape_arctic_startup():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

    # Create a Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    url = 'https://arcticstartup.com/category/funding/'
    driver.get(url)

    # Get the page source
    page_source = driver.page_source

    # Close the webdriver
    driver.quit()

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(page_source, 'html.parser')
    articles = soup.find_all('article')

    data = []
    for article in articles:
        # Extracting data from the <a> tag within <div class="td-module-thumb">
        link_tag = article.find('div', class_='td-module-thumb').find('a', class_='td-image-wrap')

        # Checking if the link tag is found
        if link_tag:
            headline = link_tag.get('title', '').strip()
            article_link = link_tag.get('href', '')

            data.append({'headline': headline, 'link': article_link})

    return data

# Function to update Nordic Google Sheets using ezsheets
def update_google_sheets(data):
    # Replace 'Your Spreadsheet Title' with your actual spreadsheet title
    spreadsheet_title = 'Your Spreadsheet Title'
    spreadsheet = ezsheets.upload(title=spreadsheet_title)

    # Select the first sheet
    sheet = spreadsheet[0]

    # Load existing data from the sheet
    existing_data = sheet.getRows()
    existing_headlines = set(entry['headline'] for entry in existing_data)

    # TODO: Use the datetime function to add a Date and Time for when the article is uploaded to database

    # Append new data to the sheet
    for entry in data:
        if entry['headline'] not in existing_headlines:
            sheet.appendRow([entry['headline'], entry['link']])
            print(f"New article added: {entry['headline']}")

# Function to update General Google Sheet database using ezsheets
def update_general_google_sheets(data):
    # Replace 'Your General Spreadsheet Title' with your actual spreadsheet title
    general_spreadsheet_title = 'Your General Spreadsheet Title'
    general_spreadsheet = ezsheets.upload(title=general_spreadsheet_title)

    # Select the first sheet in the general spreadsheet
    general_sheet = general_spreadsheet[0]

    # Load existing data from the general sheet
    existing_general_data = general_sheet.getRows()
    existing_general_headlines = set(entry['headline'] for entry in existing_general_data)

    # TODO: Use the datetime function to add a Date and Time for when the article is uploaded to the general database

    # Append new data to the general sheet
    for entry in data:
        if entry['headline'] not in existing_general_headlines:
            general_sheet.appendRow([entry['headline'], entry['link']])
            print(f"New article added to General Sheet: {entry['headline']}")


if __name__ == "__main__":
    funding_data = scrape_arctic_startup()

    if funding_data:
        update_google_sheets(funding_data)
        update_general_google_sheets(funding_data)
    else:
        print("No data to update.")
