#! pyhton3
# brokenURL.py - finds broken URL links on a given web page

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_broken_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    for link in links:
        href = link['href']
        absolute_url = urljoin(url, href)
        try:
            link_response = requests.head(absolute_url)
            if link_response.status_code == 404:
                print(f"Broken link: {absolute_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {absolute_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:       # command line arguements have to equal to 2
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    find_broken_links(url)
