# fetch_foodbanks.py

import requests
import os

# API endpoint
url = "https://www.givefood.org.uk/api/2/locations?format=geojson"

# Local file path
output_folder = "data"
output_file = os.path.join(output_folder, "foodbanks.json")

# Ensure the data folder exists
os.makedirs(output_folder, exist_ok=True)

# Make the request
print("Downloading food bank data...")
response = requests.get(url)

# Check response
if response.status_code == 200:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Data saved to {output_file}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
