import pandas as pd

def load_data(country):
    path = f"data/{country.lower()}_clean.csv"
    df = pd.read_csv(path, parse_dates=["Timestamp"])
    return df
