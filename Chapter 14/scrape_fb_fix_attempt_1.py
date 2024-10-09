from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering (optional)
chrome_options.add_argument("--window-size=1920,1080")  # Set window size (optional)

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Access Facebook profile
driver.get('https://www.facebook.com/mahfuz.nafis.tmn')
time.sleep(5)

page_url = ''  # Enter the Facebook profile URL
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

print(f'Saved {len(post_data)} posts to banglaPosts.csv')

driver.quit()
