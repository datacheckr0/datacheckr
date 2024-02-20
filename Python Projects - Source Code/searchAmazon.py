#! python3
# searchpypi.py - Opens several search results

import requests, sys, webbrowser, bs4

print('Searching...')               # display text while downloading the search result page
res = requests.get('https://amazon.co.uk/s?k=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result
linkElems = soup.select('.a-link-normal')  # Edit for amazon HTML
numOpen = min(5, len(linkElems))    # Number of tabs to open is either 5, or length of list, whichever is smaller
for i in range(numOpen):
    urlToOpen = 'https://amazon.co.uk/s?k=' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)


# You first need to know the URL of the search result page
# requests to download page => use bs4 to find search result links in the HTML => webbrowser.open() to open links
# min() returns the smallest of the integer or float arguements it is passed

