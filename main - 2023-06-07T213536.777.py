
import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = "https://www.example.com/tax-liens"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find and extract the relevant information from the webpage
tax_liens = soup.find_all("div", class_="tax-lien")

# Process and display the scraped data
for lien in tax_liens:
    property_address = lien.find("span", class_="address").text
    lien_amount = lien.find("span", class_="amount").text

    print("Property Address:", property_address)
    print("Lien Amount:", lien_amount)
    print("-" * 30)
