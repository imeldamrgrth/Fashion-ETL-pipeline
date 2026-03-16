import pandas as pd
from utils.load_postgres import save_to_postgres

def test_load_postgres():
    df = pd.DataFrame({
        "Title": ["Test Product"],
        "Price": [10.0],
        "Rating": [4.5],
        "Colors": [2],
        "Size": ["M"],
        "Gender": ["Unisex"],
        "timestamp": ["2024-01-01"]
    })

    try:
        save_to_postgres(df)
        assert True
    except Exception:
        assert False