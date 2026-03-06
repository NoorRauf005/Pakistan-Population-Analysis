import pandas as pd
import os

DATA_FILE = "pakistan_population.csv"

def load_data():
    if not os.path.exists(DATA_FILE):
        print("Dataset file not found")
        return pd.DataFrame()

    # Read only the needed columns
    needed_columns = ["Year", "Population, total", "Population, female",
                      "Urban population", "Rural population"]
    df = pd.read_csv(DATA_FILE, usecols=needed_columns)

    # Strip whitespace
    df.columns = df.columns.str.strip()

    # Rename columns to match your code
    df.rename(columns={
        "Population, total": "Total Population",
        "Population, female": "Female Population",
        "Urban population": "Urban Population",
        "Rural population": "Rural Population"
    }, inplace=True)

    # Calculate Male Population
    df["Male Population"] = df["Total Population"] - df["Female Population"]

    # Annual Growth Rate
    df["Annual Growth Rate (%)"] = df["Total Population"].pct_change() * 100

    df.fillna(0, inplace=True)

    return df
