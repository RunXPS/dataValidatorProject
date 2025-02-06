'Selenium Practice'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# reading the list
file_path = 'AI project - Confidential UNC Startups 10162024.xls (1).csv'
companies = pd.read_csv(file_path, encoding = 'Latin1')

# dropping duplicates
companies_unique = companies.drop_duplicates(subset='Company')
company_names = companies_unique['Company']
print(company_names)
# Initialize WebDriver
service = Service(executable_path="chromedriver.exe") # Copy path to chromedriver here
driver = webdriver.Chrome()

def search_nc_businesses(company_names):
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
    results = []
    
    for company in company_names:
        try:
            # Navigate to NC Secretary of State business search page
            driver.get("https://www.sosnc.gov/online_services/search/by_title/_Business_Registration")
            
            
            select_element = driver.find_element(By.ID, 'Words')
            # Create a Select object
            select = Select(select_element)
            try:
                select.select_by_value("EXACT")
                print("Selected by exact name")
            except NoSuchElementException: # type: ignore
                print("Option not found.")

            # Locate search bar on the website
            input_element = driver.find_element(By.ID, 'SearchCriteria')
            input_element.send_keys(company, Keys.ENTER)
            
            # Wait for results and get count
            time.sleep(2)  # Brief delay to allow results to load
            
            try:
                print(f"Starting search for: {company}")
                
                # Wait for search results page to load
                time.sleep(3)  # Keep the pause for stability
                
                # Find the wrapper div and get the first span with the record count
                wrapper = driver.find_element(By.CLASS_NAME, "wrapper.pad-none")
                records_span = wrapper.find_element(By.TAG_NAME, "span")
                span_text = records_span.text
                
                number = span_text.split(":")[-1].strip()
                record_count = number if number else "0"

                if int(record_count) > 0:
                    wrapper2 = driver.find_element(By.CSS_SELECTOR, "tr[style*='border-bottom:thick']")
                    tds = wrapper2.find_elements(By.TAG_NAME, "td")

                
                results.append({
                    'company': company,
                    'result': record_count,
                    'sosid': tds[0].text if tds[0] else 'na',
                    'Date Formed': tds[1].text if tds[1] else 'na',
                    'Status': tds[2].text if tds[2] else 'na',
                    'Type': tds[3].text if tds[3] else 'na'

                })

            except Exception as e:
                print(f"Specific error: {str(e)}")
                results.append({
                    'company': company,
                    'result': 'No results found'
                })
                
        except Exception as e:
            results.append({
                'company': company,
                'result': f'Error: {str(e)}'
            })
    
    driver.quit()
    return results

search_results = search_nc_businesses(company_names)
ncsos_result = pd.DataFrame(search_results, columns=['company', 'result', 'sosid', 'Date Formed', 'Status', 'Type'])

# rename the columns to make them more consistent:
ncsos_result = ncsos_result.rename(columns={
    'company': 'Company',
    'result': 'Records_Found',
    'sosid': 'SOS_ID',
    'Date Formed': 'Date_Formed',
    'Status': 'Status',
    'Type': 'Business_Type'
})

ncsos_result.to_csv('ncsos_results.csv', index=False)
