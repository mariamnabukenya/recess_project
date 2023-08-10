import requests
from bs4 import BeautifulSoup 

import csv

url = "http://xeno-canto.org"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
name_list = soup.find("ul", class_="name-list")

# Create a list to store the extracted names
names = []

# Extract the names and store them in the list
for name in name_list.find_all("li"):
    names.append(name.text.strip())

# Define the CSV file name
csv_file_name = "names.csv"

# Write the extracted names to the CSV file
with open(csv_file_name, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name"])  # Write header
    for name in names:
        writer.writerow([name])

print("Data has been extracted and saved to", csv_file_name)