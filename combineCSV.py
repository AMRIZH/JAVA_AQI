import os
import csv

# Directory where the CSV files are stored
DATA_FOLDER = "aquired_data"
OUTPUT_FILE = os.path.join(DATA_FOLDER, "aqi_november.csv")

def combine_csv_files():
    """
    Combines all CSV files in the 'aquired_data' folder into a single file
    with an added 'city_name' column, ensuring the output file is excluded.
    """
    combined_data = []
    files_processed = 0

    # Remove existing output file to prevent conflicts
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        print(f"Deleted existing file: {OUTPUT_FILE}")

    # Iterate through all files in the folder
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".csv") and filename != "aqi_november.csv":
            file_path = os.path.join(DATA_FOLDER, filename)
            city_name = filename.split("_")[0].capitalize()  # Extract city name from file name

            # Read the CSV file and add the city_name column
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["city_name"] = city_name
                    combined_data.append(row)

            files_processed += 1

    if combined_data:
        # Create the combined CSV file
        with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = list(combined_data[0].keys())  # Use the first row's keys as column names
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(combined_data)

        print(f"Combined data from {files_processed} files into {OUTPUT_FILE}")
    else:
        print("No CSV files found to combine.")

if __name__ == "__main__":
    combine_csv_files()
