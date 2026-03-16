import pandas as pd
from utils.transform import transform_data


def test_transform():

    data = {
        "Title": ["Test Shirt"],
        "Price": ["$10"],
        "Rating": ["4.5 / 5"],
        "Colors": ["3 Colors"],
        "Size": ["Size: M"],
        "Gender": ["Gender: Men"],
        "timestamp": ["2025-01-01"]
    }

    df = pd.DataFrame(data)

    clean = transform_data(df)

    assert clean["Price"].iloc[0] == 160000