import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import time


BASE_URL = "https://fashion-studio.dicoding.dev"


def fetch_page(url: str):
    """s
    Mengambil HTML dari halaman website.
    """

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Gagal mengambil halaman: {e}")
        return None


def parse_product(card):
    """
    Parsing data produk dari card HTML.
    """

    try:
        title = card.find("h3", class_="product-title").text.strip()

        price = card.find("span", class_="price").text.strip()

        rating = card.find("p", class_="rating").text.strip()

        colors = card.find("p", class_="colors").text.strip()

        size = card.find("p", class_="size").text.strip()

        gender = card.find("p", class_="gender").text.strip()

        timestamp = datetime.now()

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "timestamp": timestamp
        }

    except AttributeError as e:
        print(f"[ERROR] Parsing gagal: {e}")
        return None


def scrape_main(total_pages: int = 50):

    all_products = []

    try:

        for page in range(1, total_pages + 1):

            url = f"{BASE_URL}/page{page}"

            html = fetch_page(url)

            if html is None:
                continue

            soup = BeautifulSoup(html, "lxml")

            cards = soup.find_all("div", class_="collection-card")

            for card in cards:

                product = parse_product(card)

                if product:
                    all_products.append(product)

            print(f"[INFO] Page {page} berhasil di-scrape")

            time.sleep(1)

        df = pd.DataFrame(all_products)

        return df

    except Exception as e:
        print(f"[ERROR] scrape_main gagal: {e}")
        return pd.DataFrame()