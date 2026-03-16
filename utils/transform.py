import pandas as pd

def transform_data(df):

    try:

        df = df.copy()

        # remove null
        df = df.dropna()

        # remove duplicate
        df = df.drop_duplicates()

        # remove invalid title
        df = df[df["Title"] != "Unknown Product"]

        # remove invalid rating
        df = df[~df["Rating"].str.contains("Invalid", na=False)]

        # CLEAN PRICE
        df["Price"] = df["Price"].str.replace("$", "", regex=False)
        df["Price"] = df["Price"].astype(float) * 16000
        df["Price"] = df["Price"].astype(int)

        # CLEAN RATING
        df["Rating"] = df["Rating"].str.replace("⭐", "", regex=False)
        df["Rating"] = df["Rating"].str.replace("/ 5", "", regex=False)
        df["Rating"] = df["Rating"].str.strip()
        df["Rating"] = df["Rating"].astype(float)

        # CLEAN COLORS
        df["Colors"] = df["Colors"].str.replace("Colors", "", regex=False)
        df["Colors"] = df["Colors"].str.replace("Color", "", regex=False)
        df["Colors"] = df["Colors"].str.replace(":", "", regex=False)
        df["Colors"] = df["Colors"].str.strip()
        df["Colors"] = df["Colors"].str.extract(r"(\d+)").astype(int)

        # CLEAN SIZE
        df["Size"] = df["Size"].str.replace("Size:", "", regex=False)
        df["Size"] = df["Size"].str.strip()

        # CLEAN GENDER
        df["Gender"] = df["Gender"].str.replace("Gender:", "", regex=False)
        df["Gender"] = df["Gender"].str.strip()

        return df

    except Exception as e:

        print("Error in transform:", e)

        return pd.DataFrame()