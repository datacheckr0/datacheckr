#! python3
# strData.py - Scrapes STR (AirBnB, Vrbo, Booking.com) data and outputs into a database (Google Sheets, MongoDB)

import os, sys
import requests, bs4, ezsheets, #json?, #bright data, #streamlit

# WORKFLOW 1:

# TODO: Go to STR website and parse HTML data for listings - Potential download STR dynamic data

# TODO: Save relevant data in bs4

# TODO: Grab data from bs4 and export into Google Sheets

    # TODO: Dynamically update Google Sheet data every 24 hours using a for loop

# WORKFLOW 2:

# TODO: Import STR website dynamic datasets

# TODO: Export relevant data to Google Sheets for future querying

    # TODO: Dynamically update Google Sheet data every 24 hours
