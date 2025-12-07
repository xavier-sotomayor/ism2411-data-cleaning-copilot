import pandas as pd
import numpy as np
import csv
print(np.__version__)

df = pd.read_csv('sales_data_raw.csv')

#Standardize column names
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.upper().str.replace(' ', '_')
    return df

df = clean_column_names(df)

#Clean the white spaces in the data
def clean_white_space(df):
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    return df

df = clean_white_space(df)

#Deal with missing values
def handle_missing_values(df):
    df = df.fillna('N/A')
    return df

df = handle_missing_values(df)

df['QTY'] = pd.to_numeric(df['QTY'], errors='coerce')
df['PRICE'] = pd.to_numeric(df['PRICE'], errors='coerce')

#Deal with rows with negative quantity or price
def remove_invalid_rows(df):
    df = df.dropna(subset=['QTY', 'PRICE'])
    df = df[(df['QTY'] >= 0) & (df['PRICE'] >= 0)]        
    return df

df = remove_invalid_rows(df)

