from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time, urllib.request
import requests
import os
import json

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.instagram.com")

time.sleep(5)
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("georgefoo782")
password.send_keys("foobar782")
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(10)
try:
    notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
except:
    print("No popup asking to save login details")

time.sleep(10)

try:
    notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
    
except:
    print("No popup asking for notification")

time.sleep(5)
searchbox=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("todayonline")
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
driver.refresh()
currenturl = driver.current_url.split('/')[-2]
print(currenturl)

posts = []
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)
        
download_url = ''
download_path = 'downloads/' + currenturl

if not os.path.isdir(download_path):
	os.makedirs(download_path)
	
driver.get(posts[0])
shortcode = driver.current_url.split("/")[-2]
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
comments = soup.find_all(class_="XQXOT")
words = []
for comment in comments:
    words.append(comment.find_all(class_='p9YgZ'))
print(words)


driver.close()