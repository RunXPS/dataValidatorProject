from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def NC_business_search(company_name: str, founders: list[str]):
    driver = webdriver.Chrome()
# <input id="SearchCriteria" name="SearchCriteria" type="text" value="" autocomplete="off">
    try:
        # Open Site
        driver.get("https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx")
        # driver.get("https://www.sosnc.gov/online_services/search/by_title/_Business_Registration")
        # Input Search
        ctl00_ContentPlaceHolder1_frmEntityName
        # search_field = driver.find_element(by=By.ID, value="SearchCriteria").send_keys(company_name)
        search_field = driver.find_element(by=By.ID, value="ctl00_ContentPlaceHolder1_frmEntityName").send_keys(company_name)
        # Submit Search
        driver.find_element(by=By.ID, value="ctl00_ContentPlaceHolder1_btnSubmit").click()
        # driver.find_element(by=By.ID, value="SubmitButton").click()
        
        print(driver.find_element(by=By.CLASS_NAME, value="java_link"))

        time.sleep(4)

    finally:
        # Close the browser
        driver.quit()

NC_business_search("Google", ["IDk"])