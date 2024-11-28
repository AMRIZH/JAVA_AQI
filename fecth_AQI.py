import requests
import json
import csv
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Replace with your API key
API_KEY = os.getenv("API_KEY")
API_URL = f"https://airquality.googleapis.com/v1/history:lookup?key={API_KEY}"

# Coordinates for Surakarta
LOCATION = {"latitude": -7.554611, "longitude": 110.804833}

# Define the date range
START_DATE = datetime(2024, 11, 1)
END_DATE = datetime(2024, 11, 2)

# Initialize CSV file
CSV_FILE = "surakarta_aqi_november_2024.csv"

def fetch_aqi_data(start_time, end_time, page_token=""):
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
        "location": LOCATION
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()

def export_to_csv(data, file_name):
    """
    Export data to a CSV file.
    """
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
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

def main():
    all_data = []
    current_date = START_DATE
    
    while current_date <= END_DATE:
        next_date = current_date + timedelta(days=1)
        page_token = ""
        
        while True:
            try:
                data = fetch_aqi_data(current_date, next_date, page_token)
                all_data.extend(data.get("hoursInfo", []))
                page_token = data.get("nextPageToken")
                if not page_token:
                    break
            except Exception as e:
                print(f"Error fetching data: {e}")
                break
        
        current_date = next_date
    
    export_to_csv(all_data, CSV_FILE)
    print(f"AQI data exported to {CSV_FILE}")

if __name__ == "__main__":
    main()
