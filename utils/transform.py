import pandas as pd
import re


USD_TO_IDR = 16000


def clean_price(price: str):

    try:
        number = float(price.replace("$", "").strip())

        return int(number * USD_TO_IDR)

    except:
        return None


def clean_rating(rating: str):

    try:
        value = rating.split("/")[0].strip()

        return float(value)

    except:
        return None


def clean_colors(colors: str):

    try:
        number = re.search(r"\d+", colors)

        return int(number.group())

    except:
        return None


def clean_size(size: str):

    try:
        return size.replace("Size: ", "").strip()

    except:
        return None


def clean_gender(gender: str):

    try:
        return gender.replace("Gender: ", "").strip()

    except:
        return None


def transform_data(df: pd.DataFrame):

    try:

        df = df.copy()

        df = df[df["Title"] != "Unknown Product"]

        df["Price"] = df["Price"].apply(clean_price)

        df["Rating"] = df["Rating"].apply(clean_rating)

        df["Colors"] = df["Colors"].apply(clean_colors)

        df["Size"] = df["Size"].apply(clean_size)

        df["Gender"] = df["Gender"].apply(clean_gender)

        df.drop_duplicates(inplace=True)

        df.dropna(inplace=True)

        df["Price"] = df["Price"].astype(int)

        df["Colors"] = df["Colors"].astype(int)

        df["Rating"] = df["Rating"].astype(float)

        df["Title"] = df["Title"].astype(str)

        df["Size"] = df["Size"].astype(str)

        df["Gender"] = df["Gender"].astype(str)

        return df

    except Exception as e:
        print(f"[ERROR] transform_data gagal: {e}")
        return pd.DataFrame()