from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://login.metafilter.com")
userElem = browser.find_element(By.ID, "user_name")
userElem.send_keys('Demi')

passwordElem = browser.find_element(By.ID, "user_pass")
passwordElem.send_keys("Password")
passwordElem.submit()
