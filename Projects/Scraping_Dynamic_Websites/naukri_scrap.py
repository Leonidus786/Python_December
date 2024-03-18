import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

# URL of the page to scrape job profiles from Naukri.com
url = "https://www.naukri.com/top-jobs-by-designations# desigtop600"

# Set the path to the ChromeDriver executable
chrome_driver_path = 'E:/Python/Projects/Scraping_Dynamic_Websites/chromedriver.exe'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode (no GUI)

# Set up Chrome service
chrome_service = ChromeService(chrome_driver_path)

# Set headers to mimic a common browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Initiating the webdriver with Chrome options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get(url)

# Pause to ensure the page is loaded (You might need to adjust this based on your internet speed)
time.sleep(5)

# Use requests library to get the page source with headers
response = requests.get(url, headers=headers)
html = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the div with id 'nameSearch' which contains job profiles
all_divs = soup.find('div', {'id': 'nameSearch'})

# Check if the div is found before proceeding
if all_divs:
    # Find all 'a' tags within the div to extract job profiles
    job_profiles = all_divs.find_all('a')

    # Printing the top ten job profiles
    count = 0
    for job_profile in job_profiles:
        print(job_profile.text)
        count += 1
        if count == 10:
            break
else:
    print("Error: 'nameSearch' div not found on the page.")

# Close the webdriver
driver.close()
