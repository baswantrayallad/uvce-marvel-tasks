import requests
from bs4 import BeautifulSoup

# Target URL (example job listing page)
url = "https://realpython.github.io/fake-jobs/"

# Add headers to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all job cards
job_cards = soup.find_all("div", class_="card-content")

# Extract details
for job in job_cards:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    print("Title:", title)
    print("Company:", company)
    print("Location:", location)
    print("-" * 40)