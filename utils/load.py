import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine


def save_to_csv(df: pd.DataFrame, filename="products.csv"):

    try:
        df.to_csv(filename, index=False)

        print("[INFO] CSV berhasil disimpan")

    except Exception as e:
        print(f"[ERROR] Gagal save CSV: {e}")


def save_to_google_sheets(df):

    try:

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "google-sheets-api.json",
            scope
        )

        client = gspread.authorize(creds)

        spreadsheet = client.open(
            "Fashion Studio ETL"
        )

        worksheet = spreadsheet.sheet1

        worksheet.clear()

        # FIX TIMESTAMP
        df["timestamp"] = df["timestamp"].astype(str)

        worksheet.update(
            [df.columns.values.tolist()] +
            df.values.tolist()
        )

        print("[INFO] Google Sheets berhasil disimpan")

    except Exception as e:

        print(f"[ERROR] Google Sheets: {e}")

def save_to_postgresql(df: pd.DataFrame):

    try:

        DATABASE_URL = (
            "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/fashion_db"
        )

        engine = create_engine(DATABASE_URL)

        df.to_sql(
            "fashion_products",
            engine,
            if_exists="replace",
            index=False
        )

        print("[INFO] PostgreSQL berhasil disimpan")

    except Exception as e:
        print(f"[ERROR] Gagal save PostgreSQL: {e}")