from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time, urllib.request
import requests

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
notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

time.sleep(10)

try:
    notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
    
except:
    print("No popup asking for notification")

time.sleep(5)
searchbox=driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("toxicstatenarrativeinsg")
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
driver.refresh()
print(driver.current_url)

#scroll
#scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#match = False
#while (match == False):
#    last_count = scrolldown
#    time.sleep(3)
#    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#    if last_count == scrolldown:
#        match = True

#get posts
posts = []
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

print(posts)
print(len(posts))

download_url = ''
for post in posts:	
	driver.get(post)
	shortcode = driver.current_url.split("/")[-2]
	time.sleep(7)
	try:
		if driver.find_element(By.CSS_SELECTOR, "img[style='object-fit: cover;']") is not None:
			download_url = driver.find_element(By.CSS_SELECTOR, "img[style='object-fit: cover;']").get_attribute('src')
			urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
		time.sleep(5)
	except:
		print(0)
		
	try:
		if driver.find_element(By.CSS_SELECTOR, "video[type='video/mp4']") is not None:
			download_url = driver.find_element(By.CSS_SELECTOR, "video[type='video/mp4']").get_attribute('src')
			urllib.request.urlretrieve( download_url, '{}.mp4'.format(shortcode))
		time.sleep(5)
	except:
		print(1)

driver.close()