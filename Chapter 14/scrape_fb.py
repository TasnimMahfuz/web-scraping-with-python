from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.facebook.com/mahfuz.nafis.tmn')
time.sleep(5)  



page_url = '' #enter the facebook profile url
driver.get(page_url)
time.sleep(5)  

scroll_pause_time = 2
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
    driver.execute_script(f"window.scrollTo(0, {screen_height}*{i});")
    time.sleep(scroll_pause_time)
    i += 1
    if i > 10:  
        break

posts = driver.find_elements(By.XPATH, '//div[@data-ad-preview="message"]')
post_data = []

for post in posts:
    try:
        message = post.text
        if any('\u0980' <= char <= '\u09FF' for char in message):
            post_data.append(message)
    except Exception as e:
        continue

df = pd.DataFrame(post_data, columns=['Post'])
df.to_csv('banglaPosts.csv', index=False)

print(f'saved {len(post_data)} to banglaPosts.csv')

driver.quit()
