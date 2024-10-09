from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

CHROMEDRIVER_PATH = ChromeDriverManager().install()
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)

print(driver.find_element(By.ID, 'content').text)  # Corrected 'By.Id' to 'By.ID'
driver.close()
