import pandas as pd
from sqlalchemy import create_engine, text
import os
import csv
import django

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
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed. Please check the file format.")
        return None

# Cleansing function
def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values with "Unknown"
def clean_categorical_data(df, column):
    # Fill missing values with "Unknown"
    df[column].fillna('Unknown', inplace=True)

    # Standardize text
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = df[column].str.strip()  # Trim whitespac
    return df

    # Save the cleaned data
    def save_data(df, filename):
        if df is not None:
            df.to_csv (filename, index=False)
        else:
            print("Error: DataFrame is None")

# Main function
def main():
    # Prompt the user for the input file path
    input_file = input("Please enter the path of the CSV file you want to import: ")
    
    # Load the data
    def load_data(file_path):
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return None

    # Extract file name without extension for table name
        table_name = os.path.splitext(os.path.basename(filePath))[0]

    # Data Cleansing
    df = load_data(input_file)
    if df is not None:
        # Clean the data
        def clean_data(df):
            df.drop_duplicates(inplace=True)    
            df.fillna(df.mean(), inplace=True)  # Fill in N/A data
            return df
        cleaned_df = clean_data(df)
        output_file = input("Please enter the desired output file name (e.g., cleaned_data.csv): ")


# Define a function to save the cleansed and formatted data to a CSV file
def save_data(df, filename):
    if df is not None:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("Error: DataFrame is None")

        saveCSV = input("Please enter the desired output file name (e.g., cleaned_data.csv): ")
        save_data(cleaned_df, saveCSV)
        print(f"Cleansed data saved to {saveCSV}")


# Save the cleansed and formatted DataFrame to 'cleaned_data.csv'
def save_data(df, filename):
    save_data(cleaned_df, {filename})

# Output the cleansed and formatted DataFrame
def print_data(df):
    if df is not None:
        print(df)
    else:
        print("Error: DataFrame is None")

# Example usage
if __name__ == "__main__":
    main()
