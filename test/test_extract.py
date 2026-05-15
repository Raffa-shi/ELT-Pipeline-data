from utils.extract import fetch_page


def test_fetch_page():

    url = "https://fashion-studio.dicoding.dev"

    result = fetch_page(url)

    assert result is not None