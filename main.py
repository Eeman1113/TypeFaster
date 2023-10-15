import time 
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

#set up the drive
browser = webdriver.Chrome()
url = "https://humanbenchmark.com/tests/typing"

browser.get(url)
time.sleep(4)
#get page source 
page_source = browser.page_source
soup = BeautifulSoup(page_source, 'html.parser')
spans = soup.find_all('span', class_="incomplete")
text_to_type = ''.join([span.get_text() for span in spans])
print(text_to_type)

# time.sleep(2)
pyautogui.write(text_to_type)
time.sleep(400000)