import pandas as pd
from sqlalchemy import create_engine, text
import os
import psycopg2
import csv
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User
from models import Members, Product, Employee

# Load the dataset, csv file
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
        
        # Fill missing values in numerical columns (both integers and floats) with "Unknown"
        for column in df.select_dtypes(include=['number']).columns:
            df[column] = df[column].astype('object')  # Convert to object type
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

    def import_data_to_postgres(csv_file_path, table_name, db_config):
    #
    Imports data from a CSV file into a PostgreSQL table.

    Args:
        csv_file_path (str): Path to the CSV file.
        table_name (str): Name of the target PostgreSQL table.
        db_config (dict): Database configuration dictionary with keys 'dbname', 'user', 'password', 'host', and 'port'.
    #
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        cursor = conn.cursor()

        # Open the CSV file
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row

            # Insert data into the table
            for row in reader:
                cursor.execute(f"""
                    INSERT INTO {table_name} (column1, column2, column3) -- adjust column names as necessary
                    VALUES (%s, %s, %s)
                """, row)

        # Commit the transaction
        conn.commit()

        print("Data imported successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Define the path to your CSV file
    csv_file_path = 'path/to/your/file.csv'

    # Define the target table name
    table_name = 'your_table_name'

    # Define your database configuration
    db_config = {
        'dbname': 'your_database_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }

    # Call the function to import data
    import_data_to_postgres(csv_file_path, table_name, db_config)
