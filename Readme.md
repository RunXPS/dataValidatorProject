##### TODOS
1) Merge Files
2) Tutorial Video
3) Pull together "Paywall Problems"



## Needed Software
1. Selenium - the web scraping software we used. Opens a window and inputs commands to navigate webpages.
2. Chromedriver - allows selenium to perform inputs and act as a user.
3. Python - the programming language used

## Instructions for NC Scraper
1. Install python selenium and pandas.
2. Look for the absolute path to the companies spreadsheet we wanted to use, and paste it onto file_path.
3. Update chrome to the latest version, then go to the following link to install chromedriver. We use the stable version. Copy the url on the corresponding platform, paste onto a new tab, and then the chromedriver should download.
https://googlechromelabs.github.io/chrome-for-testing/#stable
4. After installation, look for the absolute path to the chromedriver executable and paste it onto service.

## Instructions for Delaware Scraper
1. Install Python selenium, pandas, and Excel packages. 
2. Look for the file_path variable and input the file name you want the scraper to run through.
3. Make sure to update Chrome and then go to this link: https://googlechromelabs.github.io/chrome-for-testing/. There you will click the stable version of Chromedriver. Following that please download the link that is the same as your device and Google Chrome version. There is a great video that I will paste here that visually shows the instructions if there is any confusion: https://www.youtube.com/watch?v=NB8OceGZGjA.
4. Finally, once you have downloaded the Chrome driver, go into the folder and paste the driver file into the same folder as the Python file.
5. The output you are looking for after you run the code is a table that will pop up in your terminal. This will tell you what companies do not have any records on the Delaware entity website. You will discard those and then manually check the list of companies outputted for the companies that say they have records available.
