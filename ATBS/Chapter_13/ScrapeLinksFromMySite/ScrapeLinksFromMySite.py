import requests
from bs4 import BeautifulSoup

# URL of your site
url = "https://papadimitrioudev.netlify.app"

# Send a GET request to download the page
response = requests.get(url)
response.raise_for_status()  # Raises an error if download failed

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Print the page title if it exists
page_title = soup.find("h1")
if page_title:
    print("Page Title:", page_title.get_text())

# Find all link tags <a>
links = soup.find_all("a")

print("\nLinks found on the page:")
for link in links:
    text = link.get_text()
    href = link.get("href")
    print(f"- {text}: {href}")