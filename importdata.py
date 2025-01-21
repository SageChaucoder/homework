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

from pages.models import Employee, Product, Member

def import_csv(file_path):
    """
    Import CSV file and return data as a list of dictionaries.
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def cleanse_data(data, data_type):
    """
    Cleanse the data based on the data type.
    """
    for row in data:
        if data_type == 'employee':
            row['Name'] = row['Name'].strip()
            row['Age'] = int(row['Age'].strip())
            row['Position'] = row['Position'].strip()
            row['Department'] = row['Department'].strip()
            row['Salary'] = int(row['Salary'].strip())
        elif data_type == 'product':
            row['Name'] = row['Name'].strip()
            row['Category'] = row['Category'].strip()
            row['Price'] = float(row['Price'].strip())
            row['Quantity'] = int(row['Quantity'].strip())
        elif data_type == 'member':
            row['Name'] = row['Name'].strip()
            row['Age'] = int(row['Age'].strip())
            row['Email'] = row['Email'].strip()
            row['Location'] = row['Location'].strip()
    return data

def format_data(data):
    """
    Format the data.
    """
    # Additional formatting logic can be added here if needed
    return data

def import_data_to_db(data, data_type):
    """
    Import data into the Django database.
    """
    if data_type == 'employee':
        for row in data:
            Employee.objects.create(
                Name=row['Name'],
                Age=row['Age'],
                Position=row['Position'],
                Department=row['Department'],
                Salary=row['Salary']
            )
    elif data_type == 'product':
        for row in data:
            Product.objects.create(
                Name=row['Name'],
                Category=row['Category'],
                Price=row['Price'],
                Quantity=row['Quantity']
            )
    elif data_type == 'member':
        for row in data:
            Member.objects.create(
                Name=row['Name'],
                Age=row['Age'],
                Email=row['Email'],
                Location=row['Location']
            )

def main():
    files = [
        ('CSV files/Employees.csv', 'employee'),
        ('CSV files/Products.csv', 'product'),
        ('CSV files/Members.csv', 'member')
    ]

    for file_path, data_type in files:
        # Import CSV data
        data = import_csv(file_path)
        print(f"Data imported successfully from {file_path}!")

        # Cleanse data
        cleansed_data = cleanse_data(data, data_type)
        print(f"Data cleansed successfully for {data_type}!")

        # Format data
        formatted_data = format_data(cleansed_data)
        print(f"Data formatted successfully for {data_type}!")

        # Import data to Django database
        import_data_to_db(formatted_data, data_type)
        print(f"Data imported to database successfully for {data_type}!")

if __name__ == "__main__":
    main()