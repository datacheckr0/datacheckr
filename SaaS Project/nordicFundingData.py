#! python3
# nordicFundingData.py - Scrapes funding news from Nordic data source Arctic Startup, and updates new posts to a database

import os, sys
import requests, bs4, ezsheets, selenium, #bright data, #json?


# def Web Scraping Function():

    # TODO: Use requests to open link for funding section from data source

    # TODO: Parase web pages with funding data - HTML, or JSON

    # TODO: Create for loop to dynamically scrape pages every 24 hours

        # TODO: Download pages and save in bs4

        # TODO: Transfer relevant data to database using EZsheets



# ChatGPT Source Template - Update code with relevant HTML and titles

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import ezsheets

# Function to scrape funding news from Arctic Startup
def scrape_arctic_startup():
    url = 'https://arcticstartup.com/category/funding/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
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
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

# Function to update Google Sheets using ezsheets
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

if __name__ == "__main__":
    funding_data = scrape_arctic_startup()

    if funding_data:
        update_google_sheets(funding_data)
    else:
        print("No data to update.")
