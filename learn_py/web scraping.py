# import requests
# from bs4 import BeautifulSoup
# # Step 1: Send request
# url = "https://kryoverse.com/"
# response = requests.get(url)
# # Step 2: Parse HTML
# soup = BeautifulSoup(response.text, "html.parser")
# # Step 3: Find title
# title = soup.title.text
# print("Page Title:", title)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Step 1: Send request
import requests
from bs4 import BeautifulSoup

# Step 1: Send request
url = "https://kryoverse.com/"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Get page title
title = soup.title.text if soup.title else "No title found"
print("Page Title:", title)

# Step 4: Get *visible* text from page
# Remove scripts & styles
for script in soup(["script", "style"]):
    script.extract()

# Get text
page_text = soup.get_text(separator="\n")

# Clean up lines
lines = [line.strip() for line in page_text.split("\n") if line.strip()]
clean_text = "\n".join(lines)

print("\n===== PAGE TEXT START =====\n")
print(clean_text[:3000])   # first 3000 chars, avoid too-long output
print("\n===== PAGE TEXT END =====")
