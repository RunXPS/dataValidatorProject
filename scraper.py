'Selenium Practice'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
service = Service(executable_path="/usr/local/bin/chromedriver") # Copy path to chromedriver here
driver = webdriver.Chrome(service=service)

driver.get("https://www.sosnc.gov/online_services/search/by_title/_Business_Registration")

# Locate search bar on the website
input_element = driver.find_element(By.ID, 'SearchCriteria')
input_element.send_keys('acta solutions llc', Keys.ENTER)
time.sleep(10)

driver.quit()

