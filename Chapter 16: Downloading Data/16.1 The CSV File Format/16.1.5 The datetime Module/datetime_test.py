# Downloading Data - The CSV File Format - The datetime Module

from datetime import datetime

first_date = datetime.strptime('01-10-2024', '%d-%m-%Y')
print(first_date)