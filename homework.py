import pandas as pd
from sqlalchemy import create_engine, text
import os
import csv
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

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
        df[column] = df[column].str.strip()  # Trim whitespace

    return df

# Save the cleaned data
def save_data(df, output_file_path):
    try:
        df.to_csv(output_file_path, index=False)
        print(f"Cleaned data saved to {output_file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

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
        output_file = input("Please enter the desired output file name (e.g., cleaned_data.csv): ")

        # Save the cleaned data
        save_data(cleaned_df, output_file)

# Example usage
if __name__ == "__main__":
    main()