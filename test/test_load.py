import pandas as pd
from utils.load import save_to_csv
import os


def test_save_to_csv():

    df = pd.DataFrame({
        "Title": ["Testing"]
    })

    filename = "test_products.csv"

    save_to_csv(df, filename)

    assert os.path.exists(filename)

    os.remove(filename)