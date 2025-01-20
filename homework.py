import pandas as pd
from sqlalchemy import create_engine, text
import os
import csv
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User

# Load the dataset
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)  # Exit the program with a status code
    
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        sys.exit(1)   # Exit the program with a status code
    
    except pd.errors.ParserError:
        print("Error: The file could not be parsed. Please check the file format.")
        sys.exit(1)   # Exit the program with a status code

# Cleansing function
def clean_data(df):
    if df is not None:
        # Remove duplicates
        df = df.drop_duplicates()

        # Fill missing values with "Unknown" for object columns
        for column in df.select_dtypes(include=['object']).columns:
            df[column].fillna('Unknown', inplace=True)

        # Standardize text for object columns
        for column in df.select_dtypes(include=['object']).columns:
            df[column] = df[column].str.strip()  # Trim whitespace
        return df
    else:
        print("Error: DataFrame is None")
        return None

def save_data(cleaned_df, output_file_name):
    cleaned_df.to_csv(output_file_name, index=False)
    print(f"Data saved to {output_file_name}")

# Main function
def main():
    # Prompt the user for the input file path
    input_file = input("Please enter the path of the CSV file you want to import: ")
    
    # Load the data
    df = load_data(input_file)

    if df is not None:
    # Clean the data
        cleaned_df = clean_data(df)

    # Prompt for the output file path
    output_file_name = input("Please enter the desired output file name (e.g., cleaned_data.csv): ")

    # Save the cleaned data
    save_data(cleaned_df, output_file_name)

# Example usage
if __name__ == "__main__":
    main()
