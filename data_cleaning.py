import pandas as pd
import numpy as np
import os
print(np.__version__)

def load_data(path):
    return pd.read_csv(path)

#Standardize column names
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.upper().str.replace(' ', '_')
    return df


#Clean the white spaces in the data
def clean_white_space(df):
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    return df


#Deal with missing values
def handle_missing_values(df):
    df = df.fillna('N/A')
    return df


def convert_numeric(df):
    df['QTY'] = pd.to_numeric(df['QTY'], errors='coerce')
    df['PRICE'] = pd.to_numeric(df['PRICE'], errors='coerce')
    return df

#Deal with rows with negative quantity or price
def remove_invalid_rows(df):
    df = df.dropna(subset=['QTY', 'PRICE'])
    df = df[(df['QTY'] >= 0) & (df['PRICE'] >= 0)]        
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = clean_white_space(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = convert_numeric(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)

    df_clean.to_csv(cleaned_path, index=False)
    print("Data after cleaning:")
    print(df_clean.head())