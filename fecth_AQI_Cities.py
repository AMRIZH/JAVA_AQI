import requests
import json
import csv
import os
from datetime import datetime, timedelta
import dotenv

# Replace with your API key
API_KEY = "AIzaSyAJiTwuWQ-Fz8hiPM1327iAWgDvvzYclwI"
API_URL = f"https://airquality.googleapis.com/v1/history:lookup?key={API_KEY}"

# Directory to save the files
DATA_FOLDER = "aquired_data"

# Cities and their coordinates
CITIES = {
    "Jakarta": {"latitude": -6.19514, "longitude": 106.82272},
    "Surakarta": {"latitude": -7.55461, "longitude": 110.80483},
    "Semarang": {"latitude": -6.98417, "longitude": 110.40964},
    "Yogyakarta": {"latitude": -7.80161, "longitude": 110.37272},
    "Surabaya": {"latitude": -7.27167, "longitude": 112.724},
    "Denpasar": {"latitude": -8.66361, "longitude": 115.22167},
    "Malang": {"latitude": -7.96353, "longitude": 112.63075},
    "Tegal": {"latitude": -6.87686, "longitude": 109.11847},
    "Purwokerto": {"latitude": -7.42728, "longitude": 109.23825},
    "Bandung": {"latitude": -6.92133, "longitude": 107.632},
}

# Define the date range
START_DATE = datetime(2024, 11, 1)
END_DATE = datetime(2024, 11, 2)

def fetch_aqi_data(location, start_time, end_time, page_token=""):
    """
    Fetch AQI data from the Google API for a given time range and page token.
    """
    payload = {
        "period": {
            "startTime": start_time.isoformat() + "Z",
            "endTime": end_time.isoformat() + "Z"
        },
        "pageSize": 100,  # Adjust page size as needed
        "pageToken": page_token,
        "location": location
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()

def export_to_csv(city_name, data):
    """
    Export data to a CSV file for a specific city in the `aquired_data` folder.
    Overwrites the file if it exists.
    """
    # Ensure the folder exists
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    file_path = os.path.join(DATA_FOLDER, f"{city_name.lower().replace(' ', '_')}_aqi_november_2024.csv")
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow([
            "DateTime", "AQI", "Category", "Dominant Pollutant", 
            "Red", "Green", "Blue", "Alpha"
        ])
        # Write data rows
        for entry in data:
            for index in entry.get("indexes", []):
                color = index.get("color", {})
                writer.writerow([
                    entry["dateTime"],
                    index.get("aqi"),
                    index.get("category"),
                    index.get("dominantPollutant"),
                    color.get("red"),
                    color.get("green"),
                    color.get("blue"),
                    color.get("alpha")
                ])
    print(f"Data for {city_name} exported to {file_path}")

def main():
    for city_name, location in CITIES.items():
        print(f"Fetching AQI data for {city_name}...")
        all_data = []
        current_date = START_DATE
        
        while current_date <= END_DATE:
            next_date = current_date + timedelta(days=1)
            page_token = ""
            
            while True:
                try:
                    data = fetch_aqi_data(location, current_date, next_date, page_token)
                    all_data.extend(data.get("hoursInfo", []))
                    page_token = data.get("nextPageToken")
                    if not page_token:
                        break
                except Exception as e:
                    print(f"Error fetching data for {city_name}: {e}")
                    break
            
            current_date = next_date
        
        # Export data for the current city
        export_to_csv(city_name, all_data)

if __name__ == "__main__":
    main()
