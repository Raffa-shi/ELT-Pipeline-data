import pandas as pd
import re


USD_TO_IDR = 16000


def clean_price(price):

    try:

        number = re.sub(r"[^0-9.]", "", price)

        return int(float(number) * USD_TO_IDR)

    except:
        return None


def clean_rating(rating):

    try:

        number = re.search(r"(\d+(\.\d+)?)", rating)

        return float(number.group(1))

    except:
        return None


def clean_colors(colors):

    try:

        number = re.search(r"\d+", colors)

        return int(number.group())

    except:
        return None


def clean_size(size):

    try:

        return size.replace("Size:", "").strip()

    except:
        return None


def clean_gender(gender):

    try:

        return gender.replace("Gender:", "").strip()

    except:
        return None


def transform_data(df):

    try:

        df = df.copy()

        # REMOVE INVALID
        df = df[df["Title"] != "Unknown Product"]

        # CLEANING
        df["Price"] = df["Price"].apply(clean_price)

        df["Rating"] = df["Rating"].apply(clean_rating)

        df["Colors"] = df["Colors"].apply(clean_colors)

        df["Size"] = df["Size"].apply(clean_size)

        df["Gender"] = df["Gender"].apply(clean_gender)

        # DROP NULL
        df.dropna(inplace=True)

        # DROP DUPLICATE
        df.drop_duplicates(inplace=True)

        # TYPE CASTING
        df["Price"] = df["Price"].astype(int)

        df["Rating"] = df["Rating"].astype(float)

        df["Colors"] = df["Colors"].astype(int)

        df["Title"] = df["Title"].astype(str)

        df["Size"] = df["Size"].astype(str)

        df["Gender"] = df["Gender"].astype(str)

        return df

    except Exception as e:

        print(f"[ERROR] transform_data: {e}")

        return pd.DataFrame()