import pandas as pd
import numpy as np
import csv

with open('sales_data_raw.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = [row for row in reader]
print(data)

#Standardize column names
headers = [header.upper().replace(' ', '_') for header in headers]