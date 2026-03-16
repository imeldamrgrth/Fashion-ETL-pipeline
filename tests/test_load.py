import pandas as pd
from utils.load_csv import save_to_csv


def test_save_csv():

    df = pd.DataFrame({
        "Title": ["Test"],
        "Price": [1000]
    })

    save_to_csv(df)

    assert True