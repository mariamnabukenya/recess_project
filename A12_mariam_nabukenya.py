#import necessary libraries
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import csv

#defining url
url = "https://xeno-canto.org/api/2/recordings?query=sp"

#sending request to get data
response = requests.get(url)
content = response.text
data = response.text

#using json library to extract bird species,english names and generic names
parser = json.loads(data)
species = parser['recordings']

#storing data in lists
bird_species = []
English_name = []
Generic_name = []

for item in species:
    if item["group"] == "birds":
        bird_species.append(item["sp"])
        English_name.append(item["en"])
        Generic_name.append(item["gen"])

print(bird_species)
print(bird_generic_name)
print(bird_english_name)

# writing to a csv

csv = {
    "bird_species":bird_species,
    "English_name":English_name,
    "Generic_name":Generic_name
}

#converting the dictionary to dataframe
bird = pd.DataFrame(csv)
bird.to_csv("mariam_nabukenya")
print(bird.head(10))