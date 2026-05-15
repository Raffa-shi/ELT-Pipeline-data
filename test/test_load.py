import pandas as pd
from utils.transform import transform_data


def test_transform_data():

    data = {
        "Title": ["Kaos Polos"],
        "Price": ["$10"],
        "Rating": ["4.8 / 5"],
        "Colors": ["3 Colors"],
        "Size": ["Size: M"],
        "Gender": ["Gender: Men"],
        "timestamp": ["2026-05-15"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert result["Price"].iloc[0] == 160000
    assert result["Rating"].iloc[0] == 4.8
    assert result["Colors"].iloc[0] == 3