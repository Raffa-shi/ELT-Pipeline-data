from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import (
    save_to_csv,
    save_to_google_sheets,
    save_to_postgresql
)


def main():

    print("=" * 50)
    print("START ETL PIPELINE")
    print("=" * 50)

    # EXTRACT
    raw_df = scrape_main()

    print(f"Raw data: {raw_df.shape}")

    # TRANSFORM
    clean_df = transform_data(raw_df)

    print(f"Clean data: {clean_df.shape}")

    # LOAD
    save_to_csv(clean_df)

    save_to_google_sheets(clean_df)

    save_to_postgresql(clean_df)

    print("=" * 50)
    print("ETL PIPELINE SUCCESS")
    print("=" * 50)


if __name__ == "__main__":
    main()