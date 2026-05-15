import requests
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime


BASE_URL = "https://fashion-studio.dicoding.dev"


def fetch_page(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.text

    except Exception as e:

        print(f"[ERROR] fetch_page: {e}")

        return None


def scrape_main():

    all_products = []

    try:

        for page in range(1, 51):

            url = f"{BASE_URL}/page{page}"

            html = fetch_page(url)

            if html is None:
                continue

            soup = BeautifulSoup(html, "html.parser")

            # DEBUG
            print(f"\nSCRAPING PAGE {page}")

            cards = soup.find_all("div", class_="collection-card")

            print(f"JUMLAH CARD: {len(cards)}")

            for card in cards:

                try:

                    # DEBUG HTML CARD
                    print(card.prettify()[:300])

                    title_tag = card.find("h3")
                    price_tag = card.find("span", class_="price")

                    p_tags = card.find_all("p")

                    if (
                        title_tag is None
                        or price_tag is None
                        or len(p_tags) < 4
                    ):
                        continue

                    product = {
                        "Title": title_tag.get_text(strip=True),
                        "Price": price_tag.get_text(strip=True),
                        "Rating": p_tags[0].get_text(strip=True),
                        "Colors": p_tags[1].get_text(strip=True),
                        "Size": p_tags[2].get_text(strip=True),
                        "Gender": p_tags[3].get_text(strip=True),
                        "timestamp": datetime.now()
                    }

                    print(product)

                    all_products.append(product)

                except Exception as e:

                    print(f"[ERROR] parsing card: {e}")

            print(f"[INFO] PAGE {page} selesai")

        df = pd.DataFrame(all_products)

        return df

    except Exception as e:

        print(f"[ERROR] scrape_main: {e}")

        return pd.DataFrame()