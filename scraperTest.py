#! python3
# scraperTest.py - Tests the scarping functionality
# Change the css selector and get attribute to updated Selenium functions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_arctic_startup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://arcticstartup.com/category/funding/'
    driver.get(url)

    time.sleep(5)


    # Use Selenium to find all the articles on the page
    article_elements = driver.find_elements(By.CSS_SELECTOR, "article")

    data = []
    for article_element in article_elements:
        # Use Selenium to find the link element within the article
        link_element = article_element.find_element(By.CSS_SELECTOR, 'div.td-module-thumb a.td-image-wrap')

        print(link_element)

        headline = link_element.get_attribute('title').strip()
        article_link = link_element.get_attribute('href')

        print(headline)
        print(article_link)

        data.append({'headline': headline, 'link': article_link})

    print('Now returning information')
    print(data)

    driver.quit()

    return data

if __name__ == "__main__":
    funding_data = scrape_arctic_startup()
