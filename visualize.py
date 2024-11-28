import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Read the CSV file and strip any extra whitespace in column names
    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()  # Clean column names
    return data

def plot_city_aqi(city_data, city_name):
    # Convert 'DateTime' column to datetime format
    city_data['DateTime'] = pd.to_datetime(city_data['DateTime'])
    
    # Plot AQI data for the city
    plt.figure(figsize=(10, 6))
    plt.plot(city_data['DateTime'], city_data['AQI'], marker='o', linestyle='-', color='b')
    plt.title(f"Air Quality Index (AQI) in {city_name} - November 2024")
    plt.xlabel('DateTime')
    plt.ylabel('AQI')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot AQI Categories (Good, Moderate, etc.) for the city
    plt.figure(figsize=(10, 6))
    categories = city_data['Category'].value_counts()
    categories.plot(kind='bar', color='lightblue')
    plt.title(f"AQI Categories in {city_name} - November 2024")
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_all_cities(data):
    # Convert 'DateTime' column to datetime format
    data['DateTime'] = pd.to_datetime(data['DateTime'])
    
    # Plot AQI data for all cities
    plt.figure(figsize=(12, 8))
    for city in data['city_name'].unique():
        city_data = data[data['city_name'] == city]
        plt.plot(city_data['DateTime'], city_data['AQI'], label=city)
    
    plt.title("Air Quality Index (AQI) - All Cities - November 2024")
    plt.xlabel('DateTime')
    plt.ylabel('AQI')
    plt.legend(title='City')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot AQI Categories for all cities
    plt.figure(figsize=(12, 8))
    categories = data['Category'].value_counts()
    categories.plot(kind='bar', color='lightcoral')
    plt.title("AQI Categories - All Cities - November 2024")
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Path to the combined CSV file
    file_path = 'aquired_data/aqi_november.csv'

    # Load the data
    data = load_data(file_path)
    
    # Visualize AQI data for each city
    for city in data['city_name'].unique():
        city_data = data[data['city_name'] == city]
        plot_city_aqi(city_data, city)
    
    # Visualize AQI data for all cities
    plot_all_cities(data)

if __name__ == '__main__':
    main()
