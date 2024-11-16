import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def DW_business_search(company_name: str):
    service = Service(executable_path = "chromedriver.exe")
    driver = webdriver.Chrome(service = service)
# <input id="SearchCriteria" name="SearchCriteria" type="text" value="" autocomplete="off">
    try:
        # Open Site
        driver.get("https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx")
        # driver.get("https://www.sosnc.gov/online_services/search/by_title/_Business_Registration")
        # Input Search
        # search_field = driver.find_element(by=By.ID, value="SearchCriteria").send_keys(company_name)
        search_field = driver.find_element(by=By.ID, value="ctl00_ContentPlaceHolder1_frmEntityName")
        search_field.send_keys(company_name)
        # Submit Search
        driver.find_element(by=By.ID, value="ctl00_ContentPlaceHolder1_btnSubmit").click()
        # driver.find_element(by=By.ID, value="SubmitButton").click()
        time.sleep(5)
        
        # Check for "No records found"
        try:
            no_records_element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_divCountsMsg")
            if no_records_element.is_displayed():
                return f"No records found for {company_name}."
        except:
                return f"Records available for {company_name}."
    finally:
        driver.quit
        
file_path = "AI project - Confidential UNC Startups 10162024.xls (1).csv"

try:
    # Attempt to read the file as a CSV with different encodings
    try:
        print("Trying to read the file as CSV with 'latin1' encoding...")
        df = pd.read_csv(file_path, encoding='latin1')  # Use latin1 encoding
        print("File successfully read as CSV with 'latin1' encoding.")
    except UnicodeDecodeError:
        print("Failed to read as CSV with 'latin1'. Trying with 'utf-8' and errors ignored...")
        df = pd.read_csv(file_path, encoding='utf-8', errors='ignore')  # Ignore decoding errors
        print("File successfully read as CSV with 'utf-8' and errors ignored.")
except pd.errors.ParserError:
    # If the file isn't a valid CSV, attempt to read it as an Excel file
    print("The file is not a valid CSV. Attempting to read as an Excel file...")
    try:
        df = pd.read_excel(file_path)  # Read as Excel
        print("File successfully read as an Excel file.")
    except Exception as e:
        raise ValueError(f"Failed to read the file as either CSV or Excel. Error: {e}")
results = []
for company in df.iloc[:, 0]:  # Assuming company names are in the first column
    print(f"Processing: {company}")
    result = DW_business_search(company)
    results.append({"Company Name": company, "Status": result})

results_table = pd.DataFrame(results)
output_file_path = "search_results.xlsx"
results_table.to_excel(output_file_path) #, index=False , encoding='latin1')
print(f"Search completed. Results saved to '{output_file_path}'.")