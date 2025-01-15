import pandas as pd
from sqlalchemy import create_engine, text
import os
import csv
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

# Create a connection to the database
engine = create_engine('sqlite:///db.sqlite3')

#a. Data Import and Data Cleansing
# Load the CSV file into a pandas DataFrame 

def main():
    filePath = input("Please paste your .csv path here: ") #User type in the csv file path
        
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filePath)

    # Extract file name without extension for table name
    table_name = os.path.splitext(os.path.basename(filePath))[0]

    # Data Cleansing
    # Perform data cleansing (remove duplicates)
    df.drop_duplicates(inplace=True)
    # df.fillna(df.mean(), inplace=True)  # Fill in N/A data

    print("Data cleansing complete. Here is the cleansed data:")
    print(df.head())  # Display the first few rows of the cleansed data

    saveCSV = input("Do you want to save your cleansed data file? 1 = Yes, 2 = No: ")
    if saveCSV == "1":
            output_path = 'cleansed_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Cleansed data saved to {output_path}")

#b. Data Formatting

