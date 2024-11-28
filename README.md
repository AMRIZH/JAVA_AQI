# java AQI Data

This project fetches Air Quality Index (AQI) data for multiple cities from the Google AQI API, saves the results in individual CSV files, and combines them into a single CSV file with city identifiers.

## Features

1. Fetches AQI data for specified cities over a given date range (e.g., November 2024).
2. Saves individual AQI data files for each city in the `aquired_data` folder.
3. Combines all AQI data into a single file, `aqi_november.csv`, with an added `city_name` column.

## Requirements

- Python 3.8 or higher
- Google AQI API key

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AMRIZH/JAVA_AQI.git
   cd AVA_AQI
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create the `aquired_data` folder:
   ```bash
   mkdir aquired_data
   ```

## Dependencies

The required libraries are listed in `requirements.txt`. Below are the dependencies:

- `pandas`: For data manipulation and combining CSV files.
- `requests`: For making API calls.

## Setup

1. Replace `YOUR_API_KEY` in the script with your Google AQI API key.

2. Update the list of cities in the fetch script (`aqi_fetcher.py`) as needed:
   ```python
   CITIES = [
       {"name": "Jakarta", "latitude": -6.19514, "longitude": 106.82272},
       {"name": "Surakarta", "latitude": -7.55461, "longitude": 110.80483},
       # Add more cities as needed
   ]
   ```

## Usage

### Step 1: Fetch AQI Data for Each City

Run the script to fetch AQI data for multiple cities and save individual CSV files:

```bash
python aqi_fetcher.py
```

This script will:

1. Query the Google AQI API for each city's historical AQI data.
2. Save the data as `CITYNAME_aqi_november_2024.csv` in the `aquired_data` folder.

### Step 2: Combine CSV Files

Run the script to combine all the individual CSV files into a single file:

```bash
python combine_csv.py
```

This script will:

1. Combine all CSV files in the `aquired_data` folder.
2. Add a `city_name` column to identify the source city.
3. Save the combined file as `aqi_november.csv` in the `aquired_data` folder.

### Example Output

The combined `aqi_november.csv` file will have the following structure:

| dateTime          | aqi | category              | dominantPollutant | city_name |
| ----------------- | --- | --------------------- | ----------------- | --------- |
| 2024-11-01T00:00Z | 73  | Good air quality      | pm10              | Jakarta   |
| 2024-11-01T01:00Z | 89  | Excellent air quality | o3                | Surakarta |

## Notes

- Ensure that the API key has permissions for the AQI API.
- Delete or archive previous versions of `aqi_november.csv` before running the combine script to avoid confusion.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### `requirements.txt`

```plaintext
requests
```
